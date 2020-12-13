from django.db import models
from django.contrib.auth.models import AbstractUser
import django.utils.timezone as timezone
from productApp.models import Product  

# Create your models here.
class User(AbstractUser): 
    gender = (
        ('male', '男'),
        ('female','女'),
    )
    headsculpture = models.ImageField(upload_to='headsculpture/',default="headsculpture/chicken.jpeg",verbose_name="头像")
    sex = models.CharField(max_length=32,choices=gender,default='男')
    # 使用元类在模型创建中为模型取一个别名
    
    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

class UserOrder(models.Model):
    STATUS_CHOIES = (
        (1,'待支付'),
        (2,'支付未成功'),
        (3,'运行中'),
        (4,'已取消'),
        (5,'已成功占座'),
        (6,'异常错误'),
    )
    user = models.ForeignKey(User,related_name='order_user',verbose_name='用户', on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_product',verbose_name='产品',on_delete=models.CASCADE)
    status = models.SmallIntegerField(choices=STATUS_CHOIES,default=1,verbose_name="订单状态")
    trade_no = models.CharField(max_length=128, default='', verbose_name='支付编号')
    start_time = models.DateTimeField(max_length=20,auto_now=True,verbose_name="开始时间")
    end_time = models.DateTimeField(max_length=20,auto_now_add=True,verbose_name="结束时间")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = '订单'