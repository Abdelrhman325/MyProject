from rest_framework import serializers
from .models import CustomUser, Graduation, Staff
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from apps.academics.models import Department


class CustomUserSerializer(serializers.ModelSerializer):
    repeat_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'repeat_password', 'user_type']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['repeat_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('repeat_password')
        user_type = validated_data.get('user_type')
        user = CustomUser.objects.create_user(**validated_data)

        # لو user_type = graduation يضيفه في جدول Graduation
        if user_type == 'graduation':
            Graduation.objects.create(user=user)

        return user

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['id'] = instance.id
        return rep
    


class GraduationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = Graduation
        fields = '__all__' 

    def validate(self, validated_data):
       employment_status = validated_data.get('employment_status')
       cv = validated_data.get('cv')

       if self.instance is None and not cv:
           raise serializers.ValidationError({'cv': 'This field is required.'})

       allowed_statuses = ['employee', 'unemployee', 'freelance', 'postgraduate studies']

       if self.instance is not None and employment_status is None:
           return validated_data

       if employment_status not in allowed_statuses:
           raise serializers.ValidationError({
               'employment_status': f'Invalid value. Must be one of: {", ".join(allowed_statuses)}'
        })

       if employment_status == 'employee':
           required_fields = [
            'job_name', 'location',
            'company_email', 'company_phone',
            'company_link', 'about_company'
        ]

           missing_fields = [
            field for field in required_fields
            if not validated_data.get(field) and not (self.instance and getattr(self.instance, field))
        ]

           if missing_fields:
            raise serializers.ValidationError({
                field: 'This field is required for employees.' for field in missing_fields
            })

       return validated_data


class DepartmentBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']


class StaffSerializer(serializers.ModelSerializer):
    department_detail = DepartmentBasicSerializer(source='department', many=True, read_only=True)

    class Meta:
        model = Staff
        fields = ['id', 'name', 'position', 'cv', 'image', 'department', 'department_detail']
        extra_kwargs = {
            'name': {'required': True},
            'position': {'required': True},
            'cv': {'required': True},
            'image': {'required': True},
            'department': {'required': True},
        }

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        if self.instance:
            if Staff.objects.exclude(id=self.instance.id).filter(name__iexact=value).exists():
                raise serializers.ValidationError("Staff name already exists.")
        else:
            if Staff.objects.filter(name__iexact=value).exists():
                raise serializers.ValidationError("Staff name already exists.")
        return value

    def validate_cv(self, value):
        if value and not value.name.endswith('.pdf'):
            raise serializers.ValidationError("CV must be a PDF file.")
        return value

    def validate(self, data):
        if not data.get('position'):
            raise serializers.ValidationError("Position cannot be empty.")
        return data



User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD  

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_type'] = 'Graduation' if Graduation.objects.filter(user=user).exists() else 'CustomUser'
        token['updatePassword'] = 1 if user.username == user.password else 0
        token['updateName'] = 0 if user.first_name else 1
        user.last_login = now()
        user.save(update_fields=['last_login'])
        return token
