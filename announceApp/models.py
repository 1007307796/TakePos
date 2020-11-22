from django.db import models
from DjangoUeditor.models import UEditorField
import django.utils.timezone as timezone
# Create your models here.
class AnnounceNews(models.Model):
    title = models.CharField(max_length=50,verbose_name="公告标题")
    content = UEditorField('内容',width=1000,imagePath='announce/images/',filePath='announce/files/')
    publishDate = models.DateTimeField(max_length=20,default=timezone.now,verbose_name="发布时间")
    views = models.PositiveIntegerField('浏览量',default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publishDate']
        verbose_name = '公告'
        verbose_name_plural = verbose_name
