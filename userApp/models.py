from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=16,verbose_name="用户名")
    password = models.CharField(max_length=16,verbose_name="密码")
    headsculpture = models.ImageField(upload_to='headsculpture/',blank=True,verbose_name="头像")
    email = models.EmailField(verbose_name="邮箱") 
    # 使用元类在模型创建中为模型取一个别名
    
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name