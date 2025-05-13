from datetime import datetime
from rest_framework import serializers
from .models import NewImage, NewVideo, NewsPdf, NewsArticle
from apps.units.models import unit  # تأكد من استيراد الـ unit

class NewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewImage
        fields = ['id', 'image', 'news_article']


class NewVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewVideo
        fields = ['id', 'video', 'news_article']


class NewsPdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPdf
        fields = ['id', 'pdf', 'news_article']


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = unit
        fields = ['id', 'name', 'description']


class NewsArticleSerializer(serializers.ModelSerializer):
    images = NewImageSerializer(many=True, read_only=True)
    videos = NewVideoSerializer(many=True, read_only=True)
    pdfs = NewsPdfSerializer(many=True, read_only=True)
    unit_ = UnitSerializer(many=True, read_only=True, source='units')

    class Meta:
        model = NewsArticle
        fields = [
            'id', 'ar_title', 'en_title', 'ar_description', 'en_description',
            'ar_content', 'en_content', 'ar_keywords', 'en_keywords',
            'ar_source', 'en_source', 'image', 'created_at', 'updated_at',
            'ar_new_type', 'en_new_type', 'units', 'is_active', 'is_event',
            'month', 'event_date', 'event_link', 'images', 'videos', 'pdfs',
            'unit_'
        ]


    def validate_ar_title(self, value):
        if not value:
            raise serializers.ValidationError("Arabic title is required.")
        return value

    def validate_en_title(self, value):
        if not value:
            raise serializers.ValidationError("English title is required.")
        return value

    # تحقق من أن العناوين لا تتكرر في نفس المقالة
    def validate_unique_titles(self, data):
        if data['ar_title'] == data['en_title']:
            raise serializers.ValidationError("Arabic and English titles cannot be the same.")
        return data

    # تحقق من أن الـ event_date أكبر من تاريخ اليوم
    def validate_event_date(self, value):
        if value and value < datetime.now().date():
            raise serializers.ValidationError("Event date must be a future date.")
        return value

    # تحقق مخصص للتحقق من بعض الحقول معًا
    def validate(self, data):
        # تحقق من العلاقة بين `created_at` و `event_date` (لا يمكن أن يكون الحدث في الماضي مقارنة بوقت الإنشاء)
        if data.get('event_date') and data['event_date'] < data.get('created_at', datetime.now().date()):
            raise serializers.ValidationError("Event date cannot be earlier than the creation date.")
        return data