"""webMachine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from data_process.views import (IndexView, PageView,DataPage,UserLogin,UserLoginOut,
                                UserChangePassword)
from .init_json_data import InitJsonData
from .get_veriy_img import get_verify_img
urlpatterns = [
    url(r'^$', IndexView, name='index_view'),  # 主页,测试使用
    url(r'^user_login/$', UserLogin.as_view(), name='user_login'),  # 登陆
    url(r'^get_verify_img/', get_verify_img, name='get_verify_img'),  # 验证码
    url(r'^user_change_password/$', UserChangePassword.as_view(), name='user_change_password'),  # 修改密码
    url(r'^user_login_out/$', UserLoginOut.as_view(), name='user_login_out'),  # 退出
    url(r'^page/(.+)', PageView.as_view(), name='page_view'),  # 主页,测试使用
    url(r'^initjsondata/$', InitJsonData.as_view(), name='initjsondata'),  # 主页,测试使用
    url(r'^datapage/(?P<first_catage>(.+)+)/(?P<second_catage>(.+))/', DataPage.as_view(), name='datapage'),  # 主页,测试使用

    #富文本编辑器
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
]
