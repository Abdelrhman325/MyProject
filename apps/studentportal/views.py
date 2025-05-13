# studentportal/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,filters, generics
from .models import Notification
from .serializers import NotificationSerializer
from django.db.models import Q
from project.shortcuts import IsAuth, has_permission
from .models import Studentprtal
from .serializers import StudentprtalSerializer
from django.shortcuts import get_object_or_404

class StudentPortalAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            portal = get_object_or_404(Studentprtal, pk=pk)
            serializer = StudentprtalSerializer(portal)
            return Response(serializer.data)
        portals = Studentprtal.objects.all()
        serializer = StudentprtalSerializer(portals, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)

        serializer = StudentprtalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)

        portal = get_object_or_404(Studentprtal, pk=pk)
        serializer = StudentprtalSerializer(portal, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)

        portal = get_object_or_404(Studentprtal, pk=pk)
        portal.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)












# notifications/views.py



# notifications/views.py

from rest_framework import generics, filters, status
from rest_framework.response import Response
from django.db.models import Q
from .models import Notification
from .serializers import NotificationSerializer
from project.shortcuts import IsAuth, has_permission


# إنشاء إشعار (للأدمن فقط)
class CreateNotificationView(generics.CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def create(self, request, *args, **kwargs):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        return super().create(request, *args, **kwargs)


# عرض الإشعارات الخاصة بالمستخدم (الخريج)
class UserNotificationsView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'body']

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(
            Q(receiver=user) |
            Q(send_to_all=True)
        ).order_by('-created_at')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response({'message': 'لا يوجد إشعارات'}, status=200)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



# عرض كل الإشعارات (للأدمن فقط)
class AllNotificationsView(generics.ListAPIView):
    queryset = Notification.objects.all().order_by('-created_at')
    serializer_class = NotificationSerializer

    def list(self, request, *args, **kwargs):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        return super().list(request, *args, **kwargs)


# تعديل إشعار (للأدمن فقط)
class UpdateNotificationView(generics.RetrieveUpdateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def update(self, request, *args, **kwargs):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        return super().update(request, *args, **kwargs)


# حذف إشعار (للأدمن فقط)
class DeleteNotificationView(generics.DestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def destroy(self, request, *args, **kwargs):
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        return super().destroy(request, *args, **kwargs)
