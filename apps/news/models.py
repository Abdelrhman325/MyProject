from django.db import models
from apps.units.models import unit

class NewImage(models.Model):
    image = models.ImageField(upload_to='news/images/')
    news_article = models.ForeignKey('NewsArticle', related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f"Image for {self.news_article.title}"
    
class NewVideo(models.Model):
    video = models.FileField(upload_to='news/videos/')
    news_article = models.ForeignKey('NewsArticle', related_name='videos', on_delete=models.CASCADE)

    def __str__(self):
        return f"Video for {self.news_article.title}"
    
class NewsPdf(models.Model):
    pdf = models.FileField(upload_to='news/pdfs/')
    news_article = models.ForeignKey('NewsArticle', related_name='pdfs', on_delete=models.CASCADE)

    def __str__(self):
        return f"PDF for {self.news_article.title}"

class NewsArticle(models.Model):
    
    EN_NEWS_TYPES = [
        ('ad', 'advertisement'),
        ('event', 'event'),
        ('new', 'new'),
    ]

    AR_NEWS_TYPES = [
        ('اعلان', 'اعلان'),
        ('حدث', 'حدث'),
        ('خبر', 'خبر'),
    ]

    ar_title = models.CharField(max_length=255)
    en_title = models.CharField(max_length=255)
    ar_description = models.TextField(blank=True, null=True)
    en_description = models.TextField(blank=True, null=True)
    ar_content = models.TextField()
    en_content = models.TextField()
    ar_keywords = models.JSONField(blank=True, null=True, default=list)
    en_keywords = models.JSONField(blank=True, null=True, default=list)
    ar_source = models.CharField(max_length=255, blank=True, null=True)
    en_source = models.CharField(max_length=255, blank=True, null=True)

    image = models.ImageField(upload_to='news/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ar_new_type = models.CharField(max_length=20, choices=AR_NEWS_TYPES)
    en_new_type = models.CharField(max_length=20, choices=EN_NEWS_TYPES)
    units = models.ManyToManyField(unit, related_name='news')
    is_active = models.BooleanField(default=True)
    is_event = models.BooleanField(default=False)
    month = models.PositiveIntegerField(blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)
    event_link = models.URLField(blank=True, null=True)
    def __str__(self):
        return f"{self.title} ({self.get_type_display()})"

