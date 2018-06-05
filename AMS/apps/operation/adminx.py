import xadmin

from .models import UserAssetModel


class UserAssetAdmin(object):
    list_display = ['user', 'asset_name', 'asset', 'apply_status', 'remark', 'add_time']
    list_filter = ['user', 'asset_name', 'asset', 'apply_status', 'remark']
    search_fields = ['user', 'asset_name', 'asset', 'apply_status', 'remark', 'add_time']


xadmin.site.register(UserAssetModel, UserAssetAdmin)