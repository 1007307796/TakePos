from django.db import models
from django.db.models.signals import post_init,post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime
from django.core.mail import send_mail
import os
from docxtpl import DocxTemplate,InlineImage
from docx.shared import Mm, Inches, Pt

# Create your models here.
class SchoolToPoint(models.Model):
    name = models.CharField(max_length=50,verbose_name='考点名称')
    latitude = models.DecimalField(max_digits=9,decimal_places=6,verbose_name="纬度")
    longitude = models.DecimalField(max_digits=9,decimal_places=6,verbose_name="经度")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "考点经纬度"
        verbose_name_plural = "考点经纬度"

class Feedback(models.Model):
    username = models.CharField(max_length=20,verbose_name="用户名")
    email = models.EmailField(max_length=30,verbose_name="邮箱")
    title = models.CharField(max_length=30,verbose_name="问题标题")
    fdtype = models.CharField(max_length=8,verbose_name="问题类型",default="吐槽交流")
    question = models.TextField(blank=True,null=True,verbose_name="问题详情")
    image = models.ImageField(upload_to='contact/feedback/%Y_%m_%d',verbose_name="问题截图",blank=True,null=True)
    answer = models.TextField(blank=True,null=True,verbose_name="回复")
    publishtime = models.DateTimeField(max_length=20,default=timezone.now,verbose_name="提交时间")
    replytime = models.DateTimeField(max_length=20,verbose_name="回复时间",auto_now=True,blank=True,null=True)
    status_list = (
        (1,'待审核'),
        (2,'待回复'),
        (3,'未通过'),
        (4,'已完成'),
    )
    status = models.IntegerField(choices=status_list,default=1,verbose_name="问题状态")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "工单"
        verbose_name_plural = "工单"
        ordering = ('-status','-publishtime')

class Software(models.Model):
    title = models.CharField(max_length=250,verbose_name="资料名称")
    files = models.FileField(upload_to='contact/software/',blank=True,verbose_name="文件")
    uploadtime = models.DateTimeField(max_length=20,default=timezone.now,verbose_name="上传时间")
    count = models.PositiveIntegerField('下载量',default=0) 

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-uploadtime']
        verbose_name = "文件"
        verbose_name_plural = verbose_name




@receiver(post_init,sender=Feedback)
def before_save_feedback(sender,instance,**kwargs):
    instance.__original_status = instance.status

@receiver(post_save,sender=Feedback)
def post_save_feedback(sender,instance,**kwargs):
    email = instance.email
    EMAIL_FROM = '1007307796@qq.com'
    head = '关于你在TakePos提交的' + '\"' + instance.title +'\"'
    tail = "\n\n" + "更多信息请访问TakePos官网，感谢你的来信。"
    email_title = "TakePos邮件通知"
    if (instance.__original_status == 1 or instance.__original_status == 2) and instance.status == 4:
        email_body = head + "，我们给出的答复如下:\n\n" + instance.answer + tail
        send_status = send_mail(email_title,email_body,EMAIL_FROM,[email])
        if instance.fdtype == "Bug反馈":
            base_path = os.getcwd() + '/media/contact/feedback/'
            template_path = base_path+'bug.docx'
            template = DocxTemplate(template_path)
            title = instance.title
            question = instance.question
            image = instance.image
            publishtime = instance.publishtime
            context = {
                'title': title,
                'question': question,
                'publishtime': publishtime.strftime("%Y年%m月%d日 %H:%M:%S"),
                'image': InlineImage(template,image,width=Mm(100),height=Mm(60)),
            }
            template.render(context)
            filename = base_path + datetime.strftime(datetime.now(),'%Y_%m_%d') + '/{}_{}.docx'.format(instance.title,instance.id)
            template.save(filename)
    elif instance.__original_status == 1 and instance.status == 3:
        email_body = head + "审核未通过，请写明具体信息，不要提交无关内容！" + tail
        send_status = send_mail(email_title,email_body,EMAIL_FROM,[email])