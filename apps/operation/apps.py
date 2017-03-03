# coding:utf-8
from __future__ import unicode_literals

from django.apps import AppConfig


class OperationConfig(AppConfig):
    name = 'operation'

    # 菜单栏显示中文名 init中也要配置
    verbose_name = u"用户操作"