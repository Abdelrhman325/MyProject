from urllib.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from project.shortcuts import IsAuth, get_object_or_404, has_permission
from . import models as news_models
from . import serializers as news_serializers

class NewsArticleView(APIView):

    def get(self, request, article_id=None):
        """
        Get a specific news article by ID or all articles.
        """
        if article_id:
            article = get_object_or_404(news_models.NewsArticle, id=article_id)
            serializer = news_serializers.NewsArticleSerializer(article)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        articles = news_models.NewsArticle.objects.all()
        serializer = news_serializers.NewsArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """
        Create a new news article.
        """
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        serializer = news_serializers.NewsArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, article_id):
        """
        Update a specific news article by ID.
        """
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        article = get_object_or_404(news_models.NewsArticle, id=article_id)
        serializer = news_serializers.NewsArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, article_id):
        """
        Delete a specific news article by ID.
        """
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        article = get_object_or_404(news_models.NewsArticle, id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------

class NewImage(APIView):

    def get(self, request, image_id=None, new_id=None):
        """
        Get a specific news image by ID or by news article ID.
        """
        if image_id:
            image = get_object_or_404(news_models.NewImage, id=image_id)
            serializer = news_serializers.NewImageSerializer(image)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        if new_id:
            images = news_models.NewImage.objects.filter(news_article=new_id)
            serializer = news_serializers.NewImageSerializer(images, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        images = news_models.NewImage.objects.all()
        serializer = news_serializers.NewImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """
        Create a new news image.
        """
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        serializer = news_serializers.NewImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, image_id):
        """
        Update a specific news image by ID.
        """
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        image = get_object_or_404(news_models.NewImage, id=image_id)
        serializer = news_serializers.NewImageSerializer(image, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, image_id):
        """
        Delete a specific news image by ID.
        """
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        image = get_object_or_404(news_models.NewImage, id=image_id)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------

class NewVideo(APIView):

    def get(self, request, video_id=None, new_id=None):
        """
        Get a specific news video by ID or by news article ID.
        """
        if video_id:
            video = get_object_or_404(news_models.NewVideo, id=video_id)
            serializer = news_serializers.NewVideoSerializer(video)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        if new_id:
            videos = news_models.NewVideo.objects.filter(news_article=new_id)
            serializer = news_serializers.NewVideoSerializer(videos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        videos = news_models.NewVideo.objects.all()
        serializer = news_serializers.NewVideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """
        Create a new news video.
        """
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        serializer = news_serializers.NewVideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, video_id):
        """
        Update a specific news video by ID.
        """
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        video = get_object_or_404(news_models.NewVideo, id=video_id)
        serializer = news_serializers.NewVideoSerializer(video, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, video_id):
        """
        Delete a specific news video by ID.
        """
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)
        video = get_object_or_404(news_models.NewVideo, id=video_id)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# views.py

class NewPDFView(APIView):

    def get(self, request: Request, pdf_id: int = None, new_id: int = None) -> Response:
        """
        Get a specific PDF by ID or all PDFs related to a news article.
        """

        if pdf_id:
            pdf = get_object_or_404(news_models.NewPDF, id=pdf_id)
            serializer = news_serializers.NewPDFSerializer(pdf)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if new_id:
            pdfs = news_models.NewPDF.objects.filter(news_article=new_id)
            serializer = news_serializers.NewPDFSerializer(pdfs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        pdfs = news_models.NewPDF.objects.all()
        serializer = news_serializers.NewPDFSerializer(pdfs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        """
        Upload a new PDF.
        """
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)

        serializer = news_serializers.NewsPdfSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: Request, pdf_id: int) -> Response:
        """
        Update a specific PDF by ID.
        """
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)

        pdf = get_object_or_404(news_models.NewPDF, id=pdf_id)
        serializer = news_serializers.NewsPdfSerializer(pdf, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pdf_id: int) -> Response:
        """
        Delete a specific PDF by ID.
        """
        if not IsAuth(request):
            return Response({"detail": "Authentication required"}, status=401)
        if not has_permission("core.change_visionmission", request):
            return Response({"detail": "Permission denied"}, status=403)

        pdf = get_object_or_404(news_models.NewPDF, id=pdf_id)
        pdf.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
