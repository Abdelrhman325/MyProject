from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from project.shortcuts import IsAuth, has_permission
from .models import unit, UnitService
from .serializers import UnitSerializer, UnitServiceSerializer

# API View للوحدات
class UnitListCreateAPIView(APIView):
    # عرض جميع الوحدات
    def get(self, request):
        units = unit.objects.all()
        serializer = UnitSerializer(units, many=True)
        return Response(serializer.data)

    # إنشاء وحدة جديدة
    def post(self, request):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        serializer = UnitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API View لوحدة معينة
class UnitDetailAPIView(APIView):
    # عرض وحدة معينة
    def get(self, request, pk):
        try:
            unit_obj = unit.objects.get(pk=pk)
        except unit.DoesNotExist:
            return Response({'error': 'Unit not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UnitSerializer(unit_obj)
        return Response(serializer.data)

    # تحديث وحدة معينة
    def patch(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        try:
            unit_obj = unit.objects.get(pk=pk)
        except unit.DoesNotExist:
            return Response({'error': 'Unit not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UnitSerializer(unit_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # حذف وحدة معينة
    def delete(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        try:
            unit_obj = unit.objects.get(pk=pk)
        except unit.DoesNotExist:
            return Response({'error': 'Unit not found'}, status=status.HTTP_404_NOT_FOUND)

        unit_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# API View للخدمات المرتبطة بالوحدات
class UnitServiceListCreateAPIView(APIView):
    # عرض جميع الخدمات
    def get(self, request):
        services = UnitService.objects.all()
        serializer = UnitServiceSerializer(services, many=True)
        return Response(serializer.data)

    # إضافة خدمة جديدة
    def post(self, request):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        serializer = UnitServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API View لخدمة معينة
class UnitServiceDetailAPIView(APIView):
    # عرض خدمة معينة
    def get(self, request, pk):
        try:
            service = UnitService.objects.get(pk=pk)
        except UnitService.DoesNotExist:
            return Response({'error': 'Service not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UnitServiceSerializer(service)
        return Response(serializer.data)

    # تحديث خدمة معينة
    def patch(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        try:
            service = UnitService.objects.get(pk=pk)
        except UnitService.DoesNotExist:
            return Response({'error': 'Service not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UnitServiceSerializer(service, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # حذف خدمة معينة
    def delete(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        try:
            service = UnitService.objects.get(pk=pk)
        except UnitService.DoesNotExist:
            return Response({'error': 'Service not found'}, status=status.HTTP_404_NOT_FOUND)

        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
