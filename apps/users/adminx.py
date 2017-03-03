# coding:utf-8
__author__ = 'fz'
__date__ = '2017/2/16 17:40'

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner, UserProfile
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row


class UserProfileAdmin(UserAdmin):
    # 可定制用户信息详情页面
    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             'username', 'password',
                             css_class='unsort no_title'
                             ),
                    Fieldset(_('Personal info'),
                             Row('first_name', 'last_name'),
                             'email'
                             ),
                    Fieldset(_('Permissions'),
                             'groups', 'user_permissions'
                             ),
                    Fieldset(_('Important dates'),
                             'last_login', 'date_joined'
                             ),
                ),
                Side(
                    Fieldset(_('Status'),
                             'is_active', 'is_staff', 'is_superuser',
                             ),
                )
            )
        return super(UserAdmin, self).get_form_layout()


# 全局配置
class BaseSetting(object):
    # 修改主题
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 左上角字符
    site_title = "选课系统"
    site_footer = "选课系统"

    # 系统选项收起
    menu_style = "accordion"

class EmailVerifyRecordAdmin(object):
    # code = models.CharField(max_length=20, verbose_name=u"验证码")
    # email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    # send_type = models.CharField(choices=(("register", u"注册"), ("forget", u"找回密码")), max_length=10, verbose_name=u"验证码类型")
    # send_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")
    # 也可以用数组 list_display = ('code', 'email', 'send_type', 'send_time', )
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type', ]
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index' ]
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)


# 卸载原自带user,安装新userprofile用户管理
from django.contrib.auth.models import User
xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.unregister(User)