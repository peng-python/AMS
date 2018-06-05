from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.


class DeptModel(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, default='', verbose_name='部门名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '部门信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserProfile(AbstractUser):
    name = models.CharField(max_length=100, null=True, blank=True, default='', verbose_name='姓名')
    position = models.CharField(max_length=100, null=True, blank=True, default='', verbose_name='职位')
    mobile = models.CharField(max_length=11, null=True, blank=True, default='', verbose_name='联系电话')
    work_email = models.EmailField(max_length=100, null=True, blank=True, default='', verbose_name='工作邮箱')
    personal_email = models.EmailField(max_length=100, null=True, blank=True, default='', verbose_name='个人邮箱')
    address = models.CharField(max_length=100, null=True, blank=True, default='', verbose_name='住址')
    personal_home = models.CharField(max_length=100, default='无', null=True, blank=True, verbose_name='个人主页')
    department = models.ForeignKey(DeptModel, null=True, blank=True, default='', verbose_name='所属部门')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
