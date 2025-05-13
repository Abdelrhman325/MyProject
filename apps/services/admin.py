from django.contrib import admin

# Register your models here.
from .models import section,services

admin.site.register(section)
admin.site.register(services)
