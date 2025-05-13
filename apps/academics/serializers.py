from rest_framework import serializers
from .models import Department, SpecialProgram, MastersProgram
from apps.users.models import Staff 

class StaffMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('id', 'cv', 'position', 'image', 'name')


class DepartmentSerializer(serializers.ModelSerializer):
    doctors = serializers.PrimaryKeyRelatedField(many=True, queryset=Staff.objects.all(), required=False)
    doctors_detail = StaffMiniSerializer(source='doctors', many=True, read_only=True)

    class Meta:
        model = Department
        fields = [
            'id', 'name', 'about', 'image', 'vision', 'mission',
            'doctors', 'doctors_detail',
            'pdf', 'created_at', 'updated_at',
        ]
        read_only_fields = ('created_at', 'updated_at')

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("The department name cannot be empty.")

        if self.instance:
            if Department.objects.exclude(id=self.instance.id).filter(name__iexact=value).exists():
                raise serializers.ValidationError("A department with this name already exists.")
        else:
            if Department.objects.filter(name__iexact=value).exists():
                raise serializers.ValidationError("A department with this name already exists.")
        return value

    def validate_pdf(self, value):
        if value and not value.name.endswith('.pdf'):
            raise serializers.ValidationError("The uploaded file must be a PDF.")
        return value

    def validate_doctors(self, value):
        if not value:
            raise serializers.ValidationError("At least one doctor must be assigned to the department.")
        return value

    def validate(self, data):
        if not data.get('vision') or not data.get('mission'):
            raise serializers.ValidationError("Vision and mission cannot be empty.")
        return data

    def create(self, validated_data):
        doctors = validated_data.pop('doctors', [])
        department = Department.objects.create(**validated_data)
        department.doctors.set(doctors)

        # مزامنة العلاقة العكسية
        for doctor in doctors:
            doctor.department.add(department)

        return department

    def update(self, instance, validated_data):
        doctors = validated_data.pop('doctors', None)
        instance = super().update(instance, validated_data)

        if doctors is not None:
            instance.doctors.set(doctors)

            # إزالة العلاقة القديمة
            for staff in Staff.objects.all():
                staff.department.remove(instance)

            # إضافة العلاقة الجديدة
            for doctor in doctors:
                doctor.department.add(instance)

        return instance

class SpecialProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialProgram
        fields = '__all__'
        # التحقق من أن البرنامج ليس فارغًا
    def validate(self, data):
        if not data.get('name'):
            raise serializers.ValidationError("Program name is required.")
        return data


# Masters Program Serializer
class MastersProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = MastersProgram
        fields = '__all__'
            # التحقق من أن البرنامج له اسم
    def validate(self, data):
        if not data.get('name'):
            raise serializers.ValidationError("Masters program name is required.")
        return data