# coding:utf-8
# 基于函数来做的，推荐用基于类来做
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .models import UserProfile


# 重定义登陆验证 或和与的查询条件写法
# UserProfile.objects.get(Q(username=username) | Q(email=username), Q(password=password)
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# Create your views here.
def user_login(request):
    if request.method == "POST":
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        # authenticate登陆验证方法
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            # login 登陆信息写入session
            login(request, user)
            return render(request, "index.html")
        else:
            return render(request, "login.html", {"msg": "用户名或密码错误！"})
    elif request.method == "GET":
        return render(request, "login.html")
