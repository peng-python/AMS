from django.db import models
from datetime import datetime

# Create your models here.


class FirstCategoryModel(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, default='', verbose_name='一级分类')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '资产一级类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SecondCategoryModel(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, default='', verbose_name='二级分类')
    parent_category = models.ForeignKey(FirstCategoryModel, null=True, blank=True, default='', verbose_name='所属父类')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '资产二级类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class AssetsModel(models.Model):
    ASSETS_STATUS = (
        ('IDLE', '闲置'),
        ('IN_USE', '在用'),
        ('SCRAP', '报废'),
        ('NOT_HAVE', '暂无,需购买'),
    )

    name = models.CharField(max_length=50, null=True, blank=True, default='', verbose_name='资产名称')
    category = models.ForeignKey(SecondCategoryModel, null=True, blank=True, verbose_name='所属分类')
    brand = models.CharField(max_length=50, null=True, blank=True, default='', verbose_name='品牌名称')
    assets_type = models.CharField(max_length=50, null=True, blank=True, default='', verbose_name='型号')
    assets_sn = models.CharField(max_length=50, null=True, blank=True, default='', verbose_name='资产唯一编号')
    status = models.CharField(max_length=30, choices=ASSETS_STATUS, default='IDLE', null=True, blank=True,
                              verbose_name='资产状态')
    price = models.FloatField(default=0, null=True, blank=True, verbose_name='资产价格')
    nums = models.IntegerField(default=0, null=True, blank=True, verbose_name='资产剩余可用')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '资产详细信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name