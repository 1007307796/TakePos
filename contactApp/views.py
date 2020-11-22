from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import StreamingHttpResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import SchoolToPoint,Software
from .forms import FeedbackForm
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import numpy as np
import urllib
import base64
import json
import cv2
import os


# Create your views here.
def help(request):
    return render(request,'help.html',{
        'active_menu' : 'contact',
    })

def message(request):
    if request.method == 'POST':
        feedbackForm = FeedbackForm(data=request.POST,files=request.FILES)
        print(feedbackForm.errors)
        if feedbackForm.is_valid():
            
            feedbackForm.save()
            return render(request,'success.html')
    else:
        feedbackForm = FeedbackForm()
    return render(request,'message.html',{
        'feedbackForm':feedbackForm,
        'active_menu' : 'contact',
    })
def more(request):
    return render(request,'more.html',{
        'active_menu' : 'contact',
    })

def download(request):
    softwareList = Software.objects.all()
    paginator = Paginator(softwareList, 1)
    page = request.GET.get('page')
    try:
        softwareList = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户请求的页码号不是整数，显示第一页
        softwareList = paginator.page(1)
    except EmptyPage:
        # 如果用户请求的页码号超过了最大页码号，显示最后一页
        softwareList = paginator.page(paginator.num_pages)

    return render(
        request,'download.html',{
            'softwareList': softwareList,
            'active_menu' : 'contact',
    })

def read_file(file_name,size):
    with open(file_name,mode='rb') as fp:
        while True:
            c = fp.read(size)
            if c:
                yield c
            else:
                break

def getFile(request,id):
    software = get_object_or_404(Software,id=id)
    software.count += 1
    software.save()
    headpath,filename = str(software.files).split('/')[0],str(software.files).split('/')[-1]
    filepath = "{}/media/{}/software/{}".format(os.getcwd(),headpath,filename)
    # print(filepath)
    response = StreamingHttpResponse(read_file(filepath,512))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
    return response

def buyermap(request):
    points = SchoolToPoint.objects.all()
    datalist = []
    for item in points:
        data = {}
        data['name'] = item.name
        data['latitude'] = float(item.latitude)
        data['longitude'] = float(item.longitude)
        datalist.append(data)

    return render(request,'buyermap.html',{
        'point':datalist,
    })

def platform(request):
    return render(request, 'platform.html',{
        'active_menu' : 'contact',
    })
    return HttpResponse(html)


face_detector_path = "contactApp\haarcascade_frontalface_default.xml"
face_detector = cv2.CascadeClassifier(face_detector_path)

@csrf_exempt
def facedetect(request):
    result = {}

    if request.method == "POST":
        if request.FILES.get('image') is not None:  #
            img = read_image(stream=request.FILES["image"])
        else:
            result["#faceNum"] = -1
            return JsonResponse(default)

        if img.shape[2] == 3:
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 彩色图像转灰度图像
        else:
            imgGray = img

        #进行人脸检测
        values = face_detector.detectMultiScale(imgGray,
                                           scaleFactor=1.1,
                                           minNeighbors=5,
                                           minSize=(30, 30),
                                           flags=cv2.CASCADE_SCALE_IMAGE)

        #将检测得到的人脸检测关键点坐标封装
        values = [(int(a), int(b), int(a + c), int(b + d))
                  for (a, b, c, d) in values]

        # 将检测框显示在原图上
        for (w, x, y, z) in values:
            cv2.rectangle(img, (w, x), (y, z), (0, 255, 0), 2)

        retval, buffer_img = cv2.imencode('.jpg', img)  # 在内存中编码为jpg格式
        img64 = base64.b64encode(buffer_img)  # base64编码用于网络传输
        img64 = str(img64, encoding='utf-8')  # bytes转换为str类型
        result["img64"] = img64  # json封装
    return JsonResponse(result)

def read_image(stream = None):
    if stream is not None:
        data_temp = stream.read()
    img = np.asarray(bytearray(data_temp),dtype="uint8")
    img = cv2.imdecode(img,cv2.IMREAD_COLOR)
    return img