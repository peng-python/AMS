# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-29 21:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='资产名称')),
                ('brand', models.CharField(max_length=50, verbose_name='品牌名称')),
                ('assets_type', models.CharField(max_length=50, verbose_name='型号')),
                ('assets_sn', models.CharField(default='', max_length=50, verbose_name='资产唯一编号')),
                ('status', models.CharField(choices=[('IDLE', '闲置'), ('IN_USE', '在用'), ('SCRAP', '报废'), ('NOT_HAVE', '暂无,需购买')], default='IDLE', max_length=30, verbose_name='资产状态')),
                ('price', models.FloatField(default=0, verbose_name='资产价格')),
                ('nums', models.IntegerField(default=0, verbose_name='资产剩余可用')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '资产详细信息',
                'verbose_name_plural': '资产详细信息',
            },
        ),
        migrations.CreateModel(
            name='FirstCategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='一级分类')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '资产一级类别',
                'verbose_name_plural': '资产一级类别',
            },
        ),
        migrations.CreateModel(
            name='SecondCategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='二级分类')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('parent_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.FirstCategoryModel', verbose_name='所属父类')),
            ],
            options={
                'verbose_name': '资产二级类别',
                'verbose_name_plural': '资产二级类别',
            },
        ),
        migrations.AddField(
            model_name='assetsmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.SecondCategoryModel', verbose_name='所属分类'),
        ),
    ]
