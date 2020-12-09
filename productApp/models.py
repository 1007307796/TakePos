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
    MODEL_CHOICES = (
        ('yzw',
        """
# YZW
# 请替换双引号的内的相应内容
SFZ = "532225199810140369" # 身份证/手机号
DLMM = "421519" # 登陆密码
BKSF = "江苏省" # 报考省份
BKXX = "南京航空航天大学" # 报考学校
KSFS = "全国统一考试" # 考试方式
ZXJH = "无" # 专项计划
BKLB = "非定向就业" # 报考类别
BKYX = "自动化学院" # 报考院系
# !请注意区分专硕与学硕
BKZY = "电子信息" # 报考专业
YJFX = "控制系统应用工程" # 研究方向
XXFS = "全日制" # 学习方式
# !若研招网下拉框有多条数据，请输入区别于其他考试科目的具体科目名称
KSKM = "(101)思想政治理论" # 考试科目
BKDSF = "湖南省" # 报考点省份
BKDXX = "湖南科技大学" # 报考点学校
# !若不填写，则由客服微信消息通知
SJR = "1007307796@qq.com" # 收件人,目前只支持QQ邮箱
        """),
        ('amac',
        """
# AMAC
# 请替换双引号的内的相应内容
YHM = "620102200010211128" # 身份证/手机号
DLMM = "319379yy" # 登陆密码
DQDM1 = '3' # 地区代码1
DQDM2 = '3526' # 地区代码2
DQDM3 = '1131' # 地区代码3
# !若不填写，则由客服微信消息通知
SJR = "1007307796@qq.com" # 收件人,目前只支持QQ邮箱 
        """)
    )
    title = models.CharField(choices=CLASS_ID,max_length=50,verbose_name='服务名称')
    website = models.URLField(verbose_name="网址")
    warninfo = models.TextField(verbose_name="使用注意",default="暂无注意事项") 
    textModel = models.TextField(choices=MODEL_CHOICES,verbose_name="模板",default="")
    imageCover = models.ImageField(upload_to='product_cover/',blank=True,verbose_name="产品封面")
    productType = models.CharField(choices=PRODUCTS_CHOICES,max_length=50,verbose_name="服务类型")
    price = models.DecimalField(max_digits=5,decimal_places=1,blank=True,null=True,verbose_name="价格")
    deal = models.PositiveIntegerField('成交量',default=0)
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

