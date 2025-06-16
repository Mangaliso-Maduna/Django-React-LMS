from django.contrib import admin
from .models import User, UserProfile

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'country', 'created_at']
    search_fields = ['full_name','country']
    
admin.site.register(User)
admin.site.register(UserProfile, UserAdmin)