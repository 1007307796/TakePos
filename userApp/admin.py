from django.contrib import admin
from .models import User,UserOrder
# Register your models here.
class UserOrderInline(admin.StackedInline):
    model = UserOrder
    extra = 1 # 默认显示条数

class UserAdmin(admin.ModelAdmin):
    inlines = [UserOrderInline,]

admin.site.register(User,UserAdmin)