from django.contrib import admin
from .models import AnnounceNews
# Register your models here.
class AnnounceAdmin(admin.ModelAdmin):
    style_fields = {
        'description' : 'ueditor'
    }
admin.site.register(AnnounceNews,AnnounceAdmin)