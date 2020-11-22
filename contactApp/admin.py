from django.contrib import admin
from .models import SchoolToPoint,Feedback,Software
from django.utils.safestring import mark_safe
# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('username','email','title','fdtype','question','image_data','answer','status')
    def image_data(self,obj):
        return mark_safe('<img src="{}" width="120px"/>'.format(obj.image.url))
    image_data.short_description = '问题截图'


admin.site.register(SchoolToPoint)
admin.site.register(Software)
admin.site.register(Feedback,FeedbackAdmin)