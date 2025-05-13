from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models as core_models
from . import serializers as core_serializer
from project.shortcuts import get_object_or_404, IsAuth, has_permission

class VisionMissionView(APIView):
    def get(self, request):
        queryset = core_models.VisionMission.objects.all()
        serializer = core_serializer.VisionMissionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.add_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)

        all_messions = core_models.VisionMission.objects.all()
        if len(all_messions) >= 2:
            return Response({"detail": "You can only add 2 Vision and Mission"}, status=403)

        serializer = core_serializer.VisionMissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)

        instance = get_object_or_404(core_models.VisionMission, pk=pk)
        serializer = core_serializer.VisionMissionSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.delete_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)

        instance = get_object_or_404(core_models.VisionMission, pk=pk)
        instance.delete()
        return Response(status=204)

class SliderView(APIView):
    def get(self, request):
        queryset = core_models.slider.objects.all()
        serializer = core_serializer.SliderSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.add_slider", request):
            return Response({"detail": "Permission denied"}, status=403)

        serializer = core_serializer.SliderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_slider", request):
            return Response({"detail": "Permission denied"}, status=403)

        instance = get_object_or_404(core_models.slider, pk=pk)
        serializer = core_serializer.SliderSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.delete_slider", request):
            return Response({"detail": "Permission denied"}, status=403)

        instance = get_object_or_404(core_models.slider, pk=pk)
        instance.delete()
        return Response(status=204)

class FacultyInfoView(APIView):
    def get(self, request):
        queryset = core_models.FacultyInfo.objects.all()
        serializer = core_serializer.FacultyInfoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.add_facultyinfo", request):
            return Response({"detail": "Permission denied"}, status=403)

        serializer = core_serializer.FacultyInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_facultyinfo", request):
            return Response({"detail": "Permission denied"}, status=403)

        instance = get_object_or_404(core_models.FacultyInfo, pk=pk)
        serializer = core_serializer.FacultyInfoSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.delete_facultyinfo", request):
            return Response({"detail": "Permission denied"}, status=403)

        instance = get_object_or_404(core_models.FacultyInfo, pk=pk)
        instance.delete()
        return Response(status=204)

class StatisticsView(APIView):
    def get(self, request):
        queryset = core_models.Statistics.objects.all()
        serializer = core_serializer.StatisticsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.add_statistics", request):
            return Response({"detail": "Permission denied"}, status=403)

        serializer = core_serializer.StatisticsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_statistics", request):
            return Response({"detail": "Permission denied"}, status=403)

        instance = get_object_or_404(core_models.Statistics, pk=pk)
        serializer = core_serializer.StatisticsSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.delete_statistics", request):
            return Response({"detail": "Permission denied"}, status=403)

        instance = get_object_or_404(core_models.Statistics, pk=pk)
        instance.delete()
        return Response(status=204)

class CollegeLeadersView(APIView):
    def get(self, request):
        queryset = core_models.Collegeleaders.objects.all()
        serializer = core_serializer.CollegeleadersSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.add_collegeleaders", request):
            return Response({"detail": "Permission denied"}, status=403)

        serializer = core_serializer.CollegeleadersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_collegeleaders", request):
            return Response({"detail": "Permission denied"}, status=403)

        instance = get_object_or_404(core_models.Collegeleaders, pk=pk)
        serializer = core_serializer.CollegeleadersSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.delete_collegeleaders", request):
            return Response({"detail": "Permission denied"}, status=403)

        instance = get_object_or_404(core_models.Collegeleaders, pk=pk)
        instance.delete()
        return Response(status=204)









#الشكاوى والمقترحات


class CreateComplaintView(APIView):
    

    def post(self, request):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        serializer = core_serializer.ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ListComplaintsView(APIView):
    def get(self, request):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)

        if has_permission("core.view_complaint", request):
            complaints = core_models.Complaint.objects.select_related('user').all()
        else:
            complaints = core_models.Complaint.objects.filter(user=request.user)

        serializer = core_serializer.ComplaintSerializer(complaints, many=True)
        return Response(serializer.data)

class AdminRespondComplaintView(APIView):

    def patch(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_complaint", request):
            return Response({"detail": "Permission denied"}, status=403)
        complaint = get_object_or_404(core_models.Complaint, pk=pk)
        serializer = core_serializer.ComplaintResponseSerializer(complaint, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Response submitted."})
        return Response(serializer.errors, status=400)
    
    
class UpdateComplaintView(APIView):
    def patch(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)

        complaint = get_object_or_404(core_models.Complaint, pk=pk, user=request.user)

        serializer = core_serializer.ComplaintUpdateSerializer(complaint, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Complaint updated successfully."})
        return Response(serializer.errors, status=400)