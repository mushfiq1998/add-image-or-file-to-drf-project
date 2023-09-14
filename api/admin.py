from django.contrib import admin
from .models import Profile

# Register the Profile model with the admin site
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image'] 

admin.site.register(Profile, ProfileAdmin)