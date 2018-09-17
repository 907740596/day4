from django.shortcuts import render
from apps.denglu.models import *
from  django.http import HttpResponse
# Create your views here.
def zhu(request):
    return  render(request, "denglu1.html")
def dl(request):
    return  render(request, "denglu2.html")
def zc(request):
    return  render(request, "zhuce.html")
def  denglu(request):
    user=request.POST.get('name')
    pwd=request.POST.get('password')
    us=Deng.objects.filter(name=user)
    if us:
        pwd=Deng.objects.filter(password=pwd)
        if pwd:
            return HttpResponse("登陆成功")
        else:
            return HttpResponse("密码错误")
    else:
        return HttpResponse("用户不存在")
def  zhuce(request):
    user = request.POST.get('name')
    us = request.POST.get('password')
    Deng.objects.create(name=user, password=us)
    return HttpResponse("注册成功") and render(request, "denglu1.html")
