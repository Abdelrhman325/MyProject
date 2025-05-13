from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from project.shortcuts import IsAuth, has_permission
from .models import Department, SpecialProgram, MastersProgram
from .serializers import DepartmentSerializer, SpecialProgramSerializer, MastersProgramSerializer
from django.shortcuts import get_object_or_404
 
class DepartmentListCreateAPIView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentRetrieveUpdateDestroyAPIView(APIView):
    def get(self, request, pk):
        department = get_object_or_404(Department, pk=pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        department = get_object_or_404(Department, pk=pk)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        department = get_object_or_404(Department, pk=pk)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Special Program Views
class SpecialProgramListCreateAPIView(APIView):
    def get(self, request):
        programs = SpecialProgram.objects.all()
        serializer = SpecialProgramSerializer(programs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        serializer = SpecialProgramSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SpecialProgramRetrieveUpdateDestroyAPIView(APIView):
    def get(self, request, pk):
        program = get_object_or_404(SpecialProgram, pk=pk)
        serializer = SpecialProgramSerializer(program)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        program = get_object_or_404(SpecialProgram, pk=pk)
        serializer = SpecialProgramSerializer(program, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        program = get_object_or_404(SpecialProgram, pk=pk)
        program.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Masters Program Views
class MastersProgramListCreateAPIView(APIView):
    def get(self, request):
        programs = MastersProgram.objects.all()
        serializer = MastersProgramSerializer(programs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        serializer = MastersProgramSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MastersProgramRetrieveUpdateDestroyAPIView(APIView):
    def get(self, request, pk):
        program = get_object_or_404(MastersProgram, pk=pk)
        serializer = MastersProgramSerializer(program)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        program = get_object_or_404(MastersProgram, pk=pk)
        serializer = MastersProgramSerializer(program, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        program = get_object_or_404(MastersProgram, pk=pk)
        program.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
