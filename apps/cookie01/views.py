from django.shortcuts import render
from django.http import HttpResponse# Create your views here.
'''
request.COOKIES
获取cookie通过request
设置cookie信息通过HttpResponse对象
:key  
:value
:max_age 单位为秒 7*24*60*60
:expires 过期时间例如 date  time
:path 限制访问的cookie路径
:domain
:http_only  只能通过http请求传递

'''
def cookie_view(request):
    vale= request.COOKIES.get('hello')
    #判断请求中是否携带cookie  信息
    if vale:
        print(vale)
    else:
        resp=HttpResponse('设置cookie信息')
        resp.set_cookie('hello',value='world')

    pass

# 键值对
def     session_view(request):
    session_store=request.session
    # 返回none如果key不存在
    session_store.get('key')
    # 如果key 不存在  报错
    obj=session_store['key']
    # 赋值操作
    # key存在的时候就覆盖
    session_store['key']='123456'
    # 当key 存在就不去设置值
    session_store.setdefault('key',1111)
    # 更新操作
    session_store['key']='新值'

    # 删除操作
    del session_store['key']
    # 获取所有的键
    session_store.keys()
    # 获取所有的值
    session_store.valus()
    # 获取所有的键值
    session_store.items()
    return HttpResponse('session的基本操作')
# 对象不能转换为json数据的
# 列表 字典 str 数字类型 bool  none
# 对象必须转换为字典再生产json数据