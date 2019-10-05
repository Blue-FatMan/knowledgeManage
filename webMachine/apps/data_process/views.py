from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse
from .models import SecondCatage
from django.contrib import auth

import os

base_dir = os.path.dirname(os.path.abspath(__file__))


# Create your views here.
def IndexView(request):
    return render(request, "data_process/index.html")


# 登录模块
class UserLogin(View):
    def post(self, request):
        username = request.POST.get("data[username]")
        password = request.POST.get("data[password]")
        captcha = request.POST.get("data[captcha]")
        # 从session获取的
        server_code = request.session.get("captcha")
        # 做判断比较
        if server_code.lower() == captcha.lower():
            captcha_status = 0  # 验证码验证成功
        else:
            captcha_status = -1  # 输入验证码错误
        user_obj = auth.authenticate(username=username, password=password)
        if user_obj is not None and user_obj.is_active:
            login_status = 0
        else:
            login_status = -1
        if all((login_status == 0, captcha_status == 0)):
            # request.session["username"] = username
            auth.login(request, user_obj)
        login_result = {'login_status': login_status,
                        "captcha_status": captcha_status}
        # print(login_result)
        return HttpResponse(JsonResponse(login_result), content_type='application/json')

    def get(self, request):
        return render(request, "data_process/page/login-1.html")


# 退出模块
class UserLoginOut(View):
    def post(self, request):
        # username = request.session.get('username', '') # 查询session登陆设置
        username = request.user.username  # 查询xadmin超级登陆用户
        if username:
            auth.logout(request)
            message = 0  # 已登录，正常退出
        else:
            message = -1  # 未登录
        return HttpResponse(JsonResponse({"status": message}), content_type="application/json")


# 修改密码，普通用户使用
class UserChangePassword(View):
    def post(self, request):
        old_password = request.POST.get("data[old_password]").strip()
        new_password = request.POST.get("data[new_password]").strip()
        again_password = request.POST.get("data[again_password]").strip()
        username = request.user.username
        if username and new_password == again_password:
            user_obj = auth.authenticate(username=username, password=old_password)
            if user_obj:
                user_obj.set_password(again_password)
                user_obj.save()
                auth.logout(request)  # 密码修改成功之后退出当前登录，提示用户重新登录
                res_status = 0
            else:
                res_status = -1
        else:
            res_status = -1
        return HttpResponse(JsonResponse({"res_status": res_status}), content_type="application/json")


# 返会各静态页面
class PageView(View):
    def get(self, request, page_name):
        print("page_name", page_name)
        print("base_dir", base_dir)
        if str(page_name).split("?")[0].endswith('.html'):
            # return render_to_response("data_process/page/" + page_name,context_instance=RequestContext(request))
            return render(request, "data_process/page/" + page_name)
        else:
            pass


# 返回各二级目录静态页面数据
class DataPage(View):
    def get(self, request, first_catage, second_catage):
        print(first_catage, second_catage)
        obj = SecondCatage.objects.get(second_catage_slug=second_catage)
        # print (obj.get_second_catage_html())
        return HttpResponse(obj.get_second_catage_html())
