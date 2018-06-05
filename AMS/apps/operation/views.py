from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from users.models import UserProfile, DeptModel
from assets.models import AssetsModel
from .models import UserAssetModel

# Create your views here.


@login_required
def asset_apply(request):
    users = UserProfile.objects.all().order_by('-id')
    depts = DeptModel.objects.all().order_by('-id')
    assets = AssetsModel.objects.all().order_by('-id')
    context = {'users': users, 'depts': depts, 'assets': assets}
    return render(request, 'operation/apply_asset.html', context)


@login_required
def apply_asset(request):
    post = request.POST
    user = post.get('apply_name', '')
    asset = post.get('asset_name', '')
    remark = post.get('remark', '')

    # category2_name = SecondCategoryModel.objects.filter(name=str(category2), parent_category_id=int(category1))
    if user == '' or asset == '':
        return HttpResponse('{"status":"fail","msg":"不允许为空"}', content_type='application/json')
    user_asset = UserAssetModel()
    user_asset.user_id = user
    user_asset.asset_name = asset
    user_asset.remark = remark
    user_asset.save()
    return HttpResponse('{"status":"success","msg":"申请成功，请等待领导批准"}', content_type='application/json')


@login_required
def apply_list(request):
    applyers = UserAssetModel.objects.all().order_by('-id')
    context = {'applyers': applyers}
    return render(request, 'operation/apply_list.html', context)


@login_required
def apply_edit(request, apply_id):
    apply = UserAssetModel.objects.get(id=int(apply_id))
    assets = AssetsModel.objects.filter(status='IDLE').order_by('-id')
    context = {'apply': apply, 'assets': assets}
    return render(request, 'operation/apply_edit.html', context)


@login_required
def edit_apply(request, apply_id):
    post = request.POST
    # apply = UserAssetModel.objects.get(id=int(apply_id))#得到申请用户的信息根据传进来的申请id
    asset_sn = post.get('asset_sn', '')
    apply_status = post.get('apply_status', '1')

    apply_shiyong = post.get('shiyong', '')


    if asset_sn == '':
        return HttpResponse('{"status":"fail","msg":"资产唯一编号不允许为空"}', content_type='application/json')
    applyer = UserAssetModel.objects.get(id=int(apply_id))#得到申请用户的信息根据传进来的申请id
    applyer.asset_id = int(asset_sn)#申请用户申请的资产id
    applyer.apply_status = apply_status#申请用户申请资产状态的改变
    applyer.asset.status = apply_shiyong
    # applyer.user_id = apply.user_id
    if apply_status == '5':
        # asset = AssetsModel.objects.get(id=applyer.asset_id)
        # asset.status = 'IN_USE'
        applyer.asset.status = 'IN_USE'
        applyer.asset.save()
    #     print(applyer.asset.status)
    # asset = AssetsModel.objects.get(id=applyer.asset_id)
    # asset.status = 'IN_USE'
    applyer.save()
    return HttpResponse('{"status":"success","msg":"资产状态修改成功"}', content_type='application/json')