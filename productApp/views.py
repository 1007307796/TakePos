from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Count
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from jinja2 import Environment, FileSystemLoader
from .models import Product
import json
import os
from math import modf
from pyecharts import options as opts
from pyecharts.globals import CurrentConfig
from pyecharts.charts import Liquid,Gauge
from pyecharts import options as opts
from pyecharts.charts import PictorialBar
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from productApp.tasks import send_yzw_handler
from userApp.models import UserOrder

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./productApp/templates/echarts"))

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
def productDetail(request,id):
    product = get_object_or_404(Product,id=id)
    product.views += 1
    product.save()
    return render(request,'productDetail.html',{
        'product' : product,
    })

@login_required
def createOrder(request,id):
    # 创建订单
    user = request.user
    product = get_object_or_404(Product,id=id)
    dic = {"trade_no": 202031234029, "user":user,"product":product}
    AddOrder = UserOrder.objects.create(**dic)
    code = request.POST.get('code')
    send_yzw_handler.delay(code,AddOrder.id)
    return render(request, 'create_success.html')

def showData(request):
    data = {}
    # 数据类型 float
    SuccessRate = 1.0
    c1 = (
        Liquid(init_opts=opts.InitOpts(width="350px", height="350px"))
        .add(
            series_name="平均成功率",
            data=[SuccessRate, SuccessRate],
            tooltip_opts=liquid_format(SuccessRate),
        )
    )
    # 数据类型 hours.minute
    timeCost = 5.45
    c2 = (
        Gauge(init_opts=opts.InitOpts(width="300px", height="300px"))
        .add(
            series_name="平均成功耗时",
            data_pair=[("耗时", timeCost)],
            min_=0,
            max_=24,
            split_number=12,
            title_label_opts=opts.LabelOpts(
                font_size=20, color="#C23531",font_family="Microsoft YaHei"
            ),
            detail_label_opts=opts.GaugeDetailOpts(offset_center=[0,"30%"],formatter="{value}h"),
        )
        .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter=gauge_format(timeCost)),
        )
    )
    # 数据类型：考点+排队人数
    location = ["山西", "四川","山东"]
    values = [13, 42,2]
    c3 = (
        PictorialBar(init_opts=opts.InitOpts(height="500px"))
        .add_xaxis(location)
        .add_yaxis(
            "",
            values,
            label_opts=opts.LabelOpts(is_show=False),
            symbol_size=40,
            symbol_repeat="fixed",
            symbol_offset=[0, -5],
            is_symbol_clip=True,
            symbol="image://../../static/img/wait_people.svg",
            category_gap="10px",
            gap="10px",  
        )
        .reversal_axis()
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(is_show=False),
            yaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_show=False),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(opacity=0)
                ),
            ),
        )
    )
    points = ["四川大学","成都理工大学","湖南大学"]
    counts = [4,5,1]
    # 时.分
    cost = [4.20,0.32,7.40]
    c4 = (
        Bar()
        .add_xaxis(xaxis_data=points)
        .add_yaxis(
            series_name="总人数",
            y_axis=counts,
            yaxis_index=0,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="时耗",
            y_axis=cost,
            yaxis_index=1,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="时耗",
                type_="value",
                min_=0,
                max_=24,
                interval=4,
                axislabel_opts=opts.LabelOpts(formatter="{value}h"),
            )
        )
        .set_global_opts(
            tooltip_opts=opts.TooltipOpts(
                is_show=True, trigger="axis",formatter="{b}<br>{a0}: {c0}<br>{a1}: {c1}h"
            ),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow"),
            ),
        )
    )
    data['averageRate']=c1.render_embed()
    data['averageCost']=c2.render_embed()
    data['pointCurrent']=c3.render_embed()
    data['pointDetail']=c4.render_embed()
    return render(request,'showEcharts.html',{
        'active_menu': 'charts',
        'data': data
    })

# 图像格式化函数
def gauge_format(params):
    return '平均成功耗时需' + str(int(params)) + '时' + str(int(modf(params)[0]*100)) + '分'

def liquid_format(params):
    return '成功率超过' + str(params*100) + '%!'