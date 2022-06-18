import codecs
import os
import json
from django.http import HttpResponse
from django.shortcuts import render
from .models import Auto

def index(request):
    auto = Auto.objects.all()
    return render(request,'auto/index.html',{'auto':auto})

def like_unlike_post(request):
    with codecs.open(os.getcwd()+'/auto/data.json', 'r', 'utf_8_sig') as f:
        data = json.load(f)
    if(data["isLike"]):
        data["likes"]+=1
        data["isLike"]=False
        data["text"]="Like"
    else:
        data["likes"]-=1
        data["isLike"]=True
        data["text"]="Dislike"
    with open(os.getcwd()+'/auto/data.json', 'w') as outfile:
        json.dump(data, outfile)
    return HttpResponse(
        json.dumps({
            "status": "success",
            "likes" : data["likes"],
            "text"  : data["text"],
        }),
        content_type="application/json"
    )

def likeShow(request):
    with codecs.open(os.getcwd()+'/auto/data.json', 'r', 'utf_8_sig') as f:
        data = json.load(f)
    return HttpResponse(
        json.dumps({
            "status": "success",
            "likes" : data["likes"],
            "text"  : data["text"],
        }),
        content_type="application/json"
    )

def CheckerDocker(request):
    if request.method == 'GET':
        render(request, 'CheckerDocker.html')
    if request.method == 'POST':
        print('HAHAHA')
        render(request, 'CheckerDocker.html')
    render(request, 'CheckerDocker.html')

def Cat(request):
    if request.method == 'GET':
        render(request, 'Cat.html')
    if request.method == 'POST':
        print('HEHEHE')
        render(request, 'Cat.html')
    return HttpResponse('keke')