# coding:utf-8
__author__ = 'fz'
__date__ = '2017/2/16 17:40'
import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'image']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'image']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position']
    search_fields = ['org', 'name', 'work_company', 'work_position']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position']

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
