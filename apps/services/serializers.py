from rest_framework import serializers
from .models import section, services

class SectionMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = section
        fields = ['name', 'description', 'image']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = services
        fields = ['id', 'section', 'name', 'description', 'link', 'page']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['section'] = SectionMiniSerializer(instance.section).data
        return rep

    def validate(self, data):
        section_instance = data.get('section')
        name = data.get('name')

        if section_instance and name:
            qs = services.objects.filter(section=section_instance, name=name)
            if self.instance:
                qs = qs.exclude(id=self.instance.id)
            if qs.exists():
                raise serializers.ValidationError("اسم الخدمة مكرر في نفس القسم.")
        return data


class SectionSerializer(serializers.ModelSerializer):
    services = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = section
        fields = [
            'id', 'name', 'description', 'image', 'message', 'speech',
            'biography_link', 'organizational_structure', 'page',
            'created_at', 'updated_at', 'services'
        ]

    def get_services(self, obj):
        return ServiceSerializer(obj.services.all(), many=True).data

    def validate_name(self, value):
        qs = section.objects.filter(name=value)
        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            raise serializers.ValidationError("اسم القسم موجود بالفعل.")
        return value
