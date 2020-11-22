from django.shortcuts import render,get_object_or_404
from .models import AnnounceNews
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from pyquery import PyQuery as pq
# Create your views here.

def announce(request):
    announceList = AnnounceNews.objects.all().order_by("-publishDate")
    for announce in announceList:
        html = pq(announce.content)
        announce.outline = pq(html)('p').text()
    # 分页数
    paginator = Paginator(announceList, 2)
    page = request.GET.get('page')
    try:
        announceList = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户请求的页码号不是整数，显示第一页
        announceList = paginator.page(1)
    except EmptyPage:
        # 如果用户请求的页码号超过了最大页码号，显示最后一页
        announceList = paginator.page(paginator.num_pages)

    return render(
        request,'announceList.html',{
            'active_menu' : 'announce',
            'announceList' : announceList,
    })

def announceDetail(request,id):
    announce = get_object_or_404(AnnounceNews,id=id)
    announce.views += 1
    announce.save()
    return render(request,'announceDetail.html',{
        'active_menu' : 'announce',
        'announce' : announce
    })

