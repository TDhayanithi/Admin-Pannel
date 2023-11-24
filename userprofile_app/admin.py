# Register your models here.
# userprofile_app/admin.py
from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'company', 'about', 'areas_of_interest')

admin.site.register(UserProfile, UserProfileAdmin)
