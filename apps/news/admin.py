from django.contrib import admin

from .models import NewImage,NewsArticle,NewsPdf,NewVideo


admin.site.register(NewImage)
admin.site.register(NewsArticle)    
admin.site.register(NewsPdf)
admin.site.register(NewVideo)