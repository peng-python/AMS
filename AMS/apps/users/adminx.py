import xadmin
from xadmin import views

from .models import DeptModel


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = '资产管理系统超级管理员后台'
    site_footer = '资产管理系统·版权所有'


class DeptAdmin(object):
    list_display = ['name', 'add_time']
    list_filter = ['name']
    search_fields = ['name', 'add_time']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(DeptModel, DeptAdmin)