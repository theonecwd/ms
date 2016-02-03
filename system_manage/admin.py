from django.contrib import admin

from .models import general_user
# Register your models here.

class general_user_admin(admin.ModelAdmin):
    list_display = ('name','password')
admin.site.register(general_user,general_user_admin)
