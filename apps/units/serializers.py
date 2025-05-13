from rest_framework import serializers
from .models import unit, UnitService

# Serializer مصغر لعرض بيانات مختصرة من الوحدة
class UnitMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = unit
        fields = ['id', 'name', 'message']

class UnitServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitService
        fields = ['id', 'unit', 'name', 'description', 'link', 'page']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['unit'] = UnitMiniSerializer(instance.unit).data
        return rep

    def validate_unit(self, value):
        if not unit.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("الوحدة المختارة غير موجودة.")
        return value

    def validate_link(self, value):
        if value and not value.startswith("http"):
            raise serializers.ValidationError("الرابط يجب أن يبدأ بـ http أو https.")
        return value

    def validate(self, data):
        unit_instance = data.get("unit")
        name = data.get("name")

        if UnitService.objects.filter(unit=unit_instance, name=name).exists():
            raise serializers.ValidationError("هذه الخدمة مضافة مسبقًا لهذه الوحدة.")
        return data
# Serializer للوحدة ويعرض الخدمات المرتبطة بيها
class UnitSerializer(serializers.ModelSerializer):
    services = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = unit
        fields = ['id', 'name', 'description', 'image', 'message', 'speech',
                  'biography_link', 'organizational_structure', 'page',
                  'created_at', 'updated_at', 'services']

    def get_services(self, obj):
        return UnitServiceSerializer(obj.services.all(), many=True).data

    def validate_name(self, value):
        qs = unit.objects.filter(name=value)
        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            raise serializers.ValidationError("اسم الوحدة موجود بالفعل.")
        return value
