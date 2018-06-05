from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import FirstCategoryModel, SecondCategoryModel, AssetsModel

# Create your views here.


@login_required
def first_category(request):
    # if request.method == 'POST':
    #
    # else:
    return render(request, 'assets/first_category.html')


@login_required
def add_category1(request):
    post = request.POST
    first = post.get('first_category', '')
    category_name = FirstCategoryModel.objects.filter(name=str(first))
    if category_name or first == '':
        return HttpResponse('{"status":"fail","msg":"分类已存在，请重新输入"}', content_type='application/json')
    category = FirstCategoryModel()
    category.name = first
    category.save()
    return HttpResponse('{"status":"success","msg":"保存成功"}', content_type='application/json')


@login_required
def second_category(request):
    first_name = FirstCategoryModel.objects.all()
    context = {'first_name': first_name}
    return render(request, 'assets/second_category.html', context)


@login_required
def add_category2(request):
    post = request.POST
    category1 = post.get('first_category', '') # 前端传过来的分类一级的id
    category2 = post.get('second_category', '') # 传过来的分类二级的名称
    category2_name = SecondCategoryModel.objects.filter(name=str(category2), parent_category_id=int(category1))
    if category2_name:
        return HttpResponse('{"status":"fail","msg":"分类已存在，请重新输入"}', content_type='application/json')
    category = SecondCategoryModel()
    category.parent_category_id = int(category1)
    category.name = category2
    category.save()
    return HttpResponse('{"status":"success","msg":"二级分类信息保存成功"}', content_type='application/json')


@login_required
def assets_add(request):
    category1 = FirstCategoryModel.objects.all().order_by('-id')
    # category1 = FirstCategoryModel.objects.get(id=1)
    category2 = SecondCategoryModel.objects.all().order_by('-id')
    assets = AssetsModel.objects.all().order_by('-id')
    context = {'category1s': category1, 'category2s': category2, 'assets': assets}
    return render(request, 'assets/add_assets.html', context)


@login_required
def add_assets(request):
    post = request.POST
    name = post.get('name', '')
    category = post.get('category', '')
    brand = post.get('brand', '')
    assets_type = post.get('assets_type', '')
    assets_sn = post.get('assets_sn', '')
    asset = AssetsModel.objects.filter(assets_sn=str(assets_sn))
    if asset:
        return HttpResponse('{"status":"fail","msg":"资产唯一编号重复，请重新录入"}', content_type='application/json')
    status = post.get('status', '')
    price = post.get('price', '')
    nums = post.get('nums', '')
    assets = AssetsModel()
    assets.name = name
    assets.category_id = int(category)
    assets.brand = brand
    assets.assets_type = assets_type
    assets.assets_sn = assets_sn
    assets.status = status
    assets.price = price
    assets.nums = nums
    assets.save()
    return HttpResponse('{"status":"success","msg":"资产信息保存成功"}', content_type='application/json')