from django.urls import path
from . import views

urlpatterns = [
   
      path('articles/', views.NewsArticleView.as_view(), name='news-article-list-create'),  # GET و POST
    path('articles/<int:article_id>/', views.NewsArticleView.as_view(), name='news-article-detail'),  # GET و PATCH و DELETE
    
    # News Image URLs
    path('upload-image/', views.NewImage.as_view(), name='news-image-list-create'),  # GET و POST
    path('upload-image/<int:image_id>/', views.NewImage.as_view(), name='news-image-detail'),  # GET و PATCH و DELETE
    path('upload-image/<int:image_id>/news-article/<int:new_id>/', views.NewImage.as_view(), name='news-image-by-article'),  # Get images by news article ID
    
    # News Video URLs
    path('upload-video/', views.NewVideo.as_view(), name='news-video-list-create'),  # GET و POST
    path('upload-video/<int:video_id>/', views.NewVideo.as_view(), name='news-video-detail'),  # GET و PATCH و DELETE
    path('upload-video/<int:video_id>/news-article/<int:new_id>/', views.NewVideo.as_view(), name='news-video-by-article'),  # Get videos by news article ID
    
    # News PDF URLs
    path('upload-pdf/', views.NewPDFView.as_view(), name='news-pdf-list-create'),  # GET و POST
    path('upload-pdf/<int:pdf_id>/', views.NewPDFView.as_view(), name='news-pdf-detail'),  # GET و PATCH و DELETE
]
