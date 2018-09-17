from django.db import models

# Create your models here.
'''
1.配置
注册apps
配置数据库  初始化数据库驱动
配置static


2.创建app一个APP
就是一个模块
*****注册
    编写模型类型
    编写二级路由
'''
class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=64,unique=True)
    password=models.CharField(max_length=32)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=11)
    create_date=models.DateTimeField(auto_now_add=True)
    is_delate=models.BooleanField(default=False)
    class Meta:
        db_table="user"
        ordering=['create_date']