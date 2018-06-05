from django.db import models
from datetime import datetime

from users.models import UserProfile
from assets.models import AssetsModel

# Create your models here.


class UserAssetModel(models.Model):
    user = models.ForeignKey(UserProfile, null=True, blank=True, default='', verbose_name='用户')
    asset_name = models.CharField(max_length=100, null=False, default='', verbose_name='申请资产名称')
    asset = models.ForeignKey(AssetsModel, null=True, blank=True, default='', verbose_name='资产信息')
    apply_status = models.IntegerField(choices=((1, "审核中"), (2, "通过"), (3, "不同意"), (4, "正在配置"), (5, "已完成，正在使用")),
                                       null=True, blank=True, default=1, verbose_name=u"申请状态")
    remark = models.TextField(null=True, verbose_name='备注')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户资产信息操作'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name
