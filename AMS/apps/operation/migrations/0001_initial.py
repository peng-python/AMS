# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-29 21:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAssetModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_status', models.IntegerField(choices=[(1, '审核中'), (2, '通过'), (3, '不同意'), (4, '正在配置'), (5, '已完成，正在使用')], default=1, verbose_name='申请状态')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.AssetsModel', verbose_name='资产信息')),
            ],
            options={
                'verbose_name': '用户资产信息操作',
                'verbose_name_plural': '用户资产信息操作',
            },
        ),
    ]
