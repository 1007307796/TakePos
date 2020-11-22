from django.db import models
from django.utils import timezone

# Create your models here.
class SucceededUser(models.Model):
    user = models.ForeignKey(
        to="userApp.User",
        on_delete=models.CASCADE,
        verbose_name="用户",
        related_name="userTop",
    )
    # servicetype = models.CharField(max_length=50,verbose_name="服务类型")
    # 
    timestart = models.DateTimeField(max_length=20,default=timezone.now,verbose_name="开始时间")
    timeend = models.DateTimeField(max_length=20,default=timezone.now,verbose_name="结束时间")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "最新成交"
        verbose_name_plural = verbose_name
        ordering = ('-timeend',)

