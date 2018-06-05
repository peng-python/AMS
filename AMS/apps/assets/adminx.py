import xadmin
from .models import FirstCategoryModel, SecondCategoryModel, AssetsModel


class FirstCategoryAdmin(object):
    list_display = ['name', 'add_time']
    list_filter = ['name']
    search_fields = ['name', 'add_time']


class SecondCategoryAdmin(object):
    list_display = ['name', 'parent_category', 'add_time']
    list_filter = ['name', 'parent_category']
    search_fields = ['name', 'parent_category', 'add_time']


class AssetsAdmin(object):
    list_display = ['name', 'category', 'brand', 'assets_type', 'assets_sn', 'status', 'price', 'nums', 'add_time']
    list_filter = ['name', 'category', 'brand', 'assets_type', 'assets_sn', 'status', 'price', 'nums']
    search_fields = ['name', 'category', 'brand', 'assets_type', 'assets_sn', 'status', 'price', 'nums', 'add_time']


xadmin.site.register(FirstCategoryModel, FirstCategoryAdmin)
xadmin.site.register(SecondCategoryModel, SecondCategoryAdmin)
xadmin.site.register(AssetsModel, AssetsAdmin)