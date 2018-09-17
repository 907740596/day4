from django.shortcuts import render

# Create your views here.
from apps.main.models import Img


def index(request):
    imgs=Img.objects.all()
    return render(request,'index.html',{'imgs':imgs})