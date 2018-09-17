from django.conf.urls import url
from apps.user import views

urlpatterns=[
    url('register/',views.register,name="register"),
    url('login/',views.login),
]