from django.contrib import admin
from Dashboard.models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','photo','date']
