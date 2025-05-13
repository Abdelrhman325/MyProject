from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from project.shortcuts import IsAuth, has_permission
from .models import section, services
from .serializers import SectionSerializer, ServiceSerializer

# API View للوحدات
class SectionListCreateAPIView(APIView):
    def get(self, request):
        sections = section.objects.all()
        serializer = SectionSerializer(sections, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SectionDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            section_obj = section.objects.get(pk=pk)
        except section.DoesNotExist:
            return Response({'error': 'Section not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SectionSerializer(section_obj)
        return Response(serializer.data)

    def patch(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        try:
            section_obj = section.objects.get(pk=pk)
        except section.DoesNotExist:
            return Response({'error': 'Section not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SectionSerializer(section_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        try:
            section_obj = section.objects.get(pk=pk)
        except section.DoesNotExist:
            return Response({'error': 'Section not found'}, status=status.HTTP_404_NOT_FOUND)

        section_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# API View للخدمات
class ServiceListCreateAPIView(APIView):
    def get(self, request):
        service = services.objects.all()
        serializer = ServiceSerializer(service, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceDetailAPIView(APIView):
    def get(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        try:
            service_obj = services.objects.get(pk=pk)
        except services.DoesNotExist:
            return Response({'error': 'Service not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServiceSerializer(service_obj)
        return Response(serializer.data)

    def patch(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        try:
            service_obj = services.objects.get(pk=pk)
        except services.DoesNotExist:
            return Response({'error': 'Service not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServiceSerializer(service_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        try:
            service_obj = services.objects.get(pk=pk)
        except services.DoesNotExist:
            return Response({'error': 'Service not found'}, status=status.HTTP_404_NOT_FOUND)

        service_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
