from django.contrib import admin

# Register your models here.
from .models import Department, SpecialProgram, MastersProgram

admin.site.register(Department)
admin.site.register(SpecialProgram)
admin.site.register(MastersProgram)
