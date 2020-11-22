from django.db import models

# Create your models here.
class Product(models.Model):
    PRODUCTS_CHOICES = (
        ('education','学历类考试'),
        ('technology',"计算机类考试"),
        ('economic',"金融类考试"),
        ('language','语言类考试'),
    )
    CLASS_ID = (
        ('yzw','中国研究生招生信息网'),
        ('amac','基金从业人员资格考试')
    )
    title = models.CharField(choices=CLASS_ID,max_length=50,verbose_name='服务名称')
    website = models.URLField(verbose_name="网址")
    warninfo = models.TextField(verbose_name="使用注意",default="暂无注意事项") 
    imageCover = models.ImageField(upload_to='product_cover/',blank=True,verbose_name="产品封面")
    productType = models.CharField(choices=PRODUCTS_CHOICES,max_length=50,verbose_name="服务类型")
    price = models.DecimalField(max_digits=5,decimal_places=1,blank=True,null=True,verbose_name="价格")
    views = models.PositiveIntegerField('浏览量',default=0)

    def __str__(self):
        return self.get_title_display()
    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品'


class ProductImg(models.Model):
    product = models.ForeignKey(Product,
        related_name='productImgs',
        verbose_name='产品',
        on_delete="models.CASCADE"
    )
    photo = models.ImageField(upload_to="product/",blank=True,verbose_name="成功截图")

    def __str__(self):
        return self.product.get_title_display()

    class Meta:
        verbose_name = '成功截图'
        verbose_name_plural = verbose_name
