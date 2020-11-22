from django.contrib import admin
from .models import SucceededUser

# Register your models here.
admin.site.site_header = "Take Pos 后台管理"
admin.site.site_title = "Take Pos 后台管理"
admin.site.register(SucceededUser)