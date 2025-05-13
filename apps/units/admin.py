from django.contrib import admin

# Register your models here.
from .models import unit,UnitService

admin.site.register(unit)
admin.site.register(UnitService)

