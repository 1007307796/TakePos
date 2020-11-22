from django.shortcuts import render,get_object_or_404
from .models import Product
from django.db.models import Count
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

# Create your views here.
def products(request,productName):
    labels = []
    class Labels(object):

        def __init__(self,pid,pname,pcount):
            self.pid = pid
            self.pname = pname
            self.pcount = pcount

    productList = Product.objects.all()
    label = Labels(pid="all",pname="所有类型",pcount=len(productList))
    labels.append(label)
    label_ed = Labels(pid="education",pname="学历类考试",pcount=0)
    label_te = Labels(pid="technology",pname="计算机类考试",pcount=0)
    label_ec = Labels(pid="economic",pname="金融类考试",pcount=0)
    label_la = Labels(pid="language",pname="语言类考试",pcount=0)
    for product in productList:
        if product.productType == label_ed.pid:
            label_ed.pcount += 1
        if product.productType == label_te.pid:
            label_te.pcount += 1
        if product.productType == label_ec.pid:
            label_ec.pcount += 1
        if product.productType == label_la.pid:
            label_la.pcount += 1
    labels.extend([label_ed,label_te,label_ec,label_la])
    if productName != 'all':
        productList = Product.objects.all().filter(productType=productName)
    paginator = Paginator(productList, 1)
    page = request.GET.get('page')
    try:
        productList = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户请求的页码号不是整数，显示第一页
        productList = paginator.page(1)
    except EmptyPage:
        # 如果用户请求的页码号超过了最大页码号，显示最后一页
        productList = paginator.page(paginator.num_pages)
    return render(
        request,'productList.html',{
            'productName' : productName,
            'productList' : productList,
            'labels': labels,
    })

# def productDetail(request,id):
#     product = get_object_or_404(Product,id=id)
#     product.views += 1
#     product.save()
#     fieldsList={}
#     fieldsList[product.title]=[
#         ("报考省份","如:陕西省",""),
#         ("报考学校","如:西安电子科技大学",""),
#         ("考试方式","如:全国统一考试",""),
#         ("专项计划","如:无",""),
#         ("报考类别","如:非定向就业",""),
#         ("报考院系","如:机电工程学院",""),
#         ("报考专业","如:控制科学与工程","请注意区分专硕与学硕"),
#         ("研究方向","如:控制理论与控制工程",""),
#         ("学习方式","如:全日制",""),
#         ("考试科目","如:思想政治理论","若研招网下拉框有多条数据，请输入区别于其他考试科目的具体科目名称"),
#         ("报考点省份","如:湖南省",""),
#         ("报考点学校","如:湖南科技大学",""),
#         ("发送至此邮箱","如:1007307796@qq.com","若不填写，则由客服微信消息通知")
#     ]
#     return render(request,'productDetail.html',{
#         'fieldsList' : fieldsList[product.title],
#         'product' : product,
#     })

def productDetail(request,id):
    product = get_object_or_404(Product,id=id)
    product.views += 1
    product.save()
    return render(request,'productDetail.html',{
        'product' : product,
    })
