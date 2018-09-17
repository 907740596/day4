from django.shortcuts import render, redirect

# Create your views here.
from apps.user.models import User


def register(req):

        if req.method == "GET":
            return render(req, 'register.html')
        elif req.method == 'POST':
            username = req.POST.get('username')
            password = req.POST.get('password')
            confirm_password = req.POST.get('confirm_password')
            email = req.POST.get('email')
            phone = req.POST.get('phone')
            if password and username and email and password == confirm_password:
                users = User.objects.filter(username=username)
                if users:
                    return render(req, 'register.html', {'msg': "账号存在"})
                else:
                    user = User(username=username, password=password, email=email, phone=phone)
                    user.save()
                    return  render(req,'register.html')
            else:
                return render(req, 'register.html', {'msg': "参数不正确"})
        else:
            return render(req, 'register.html', {'msg': "不支持该方式传送"})
    # except:
    #     return render(req, 'register.html', {'msg': "服务器异常"})


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        pwd = User.objects.filter(username=username, password=password)
        if user:
            if pwd:
                return render(request, "login.html",{"msg":"登录成功"} )
            else:
                return render(request, "login.html", {"msg": "密码错误"})
        else:
            return render(request, "login.html", {"msg": "用户名不存在"})
