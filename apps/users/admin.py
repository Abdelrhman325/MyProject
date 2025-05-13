
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Graduation

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'user_type', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type',)}),
    )



class GraduationAdmin(admin.ModelAdmin):
    list_display = ['user', 'employment_status', 'job_name']


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Graduation, GraduationAdmin)
