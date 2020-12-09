from django.contrib import admin
from .models import User,UserOrder
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','password','headsculpture','email']

admin.site.register(User,UserAdmin)
admin.site.register(UserOrder)