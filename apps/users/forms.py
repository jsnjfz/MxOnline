# coding:utf-8
__author__ = 'fz'
__date__ = '2017/2/17 15:51'
from django import forms
from .models import UserProfile
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    # class Meta:
    #     model = UserProfile
    #     include = ("username", "password")
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误！"})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误！"})


class ModifyPwdForm(forms.Form):
    password = forms.CharField(required=True)
    password_re = forms.CharField(required=True)