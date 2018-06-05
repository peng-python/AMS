from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import DeptModel, UserProfile
from .forms import AddUserForm, LoginForm
from assets.models import AssetsModel, SecondCategoryModel
from operation.models import UserAssetModel

# Create your views here.


def login_user(request):
    user_form = LoginForm(request.POST)
    if user_form.is_valid():
        post = request.POST
        user_name = post.get('username', '')
        pass_word = post.get('password', '')
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated():
            users = UserProfile.objects.all().count()
            assets = AssetsModel.objects.all().count()
            apply = UserAssetModel.objects.filter(apply_status=1).count()
            category = SecondCategoryModel.objects.all().count()
            context = {'users': users, 'assets': assets, 'apply': apply, 'category': category}
            return render(request, 'index.html', context)
        else:
            return render(request, 'login.html')


@login_required
def dept(request):
    return render(request, 'users/add_dept.html')


@login_required
def add_dept(request):
    get_dept = request.POST.get('dept_name', '')
    depts = DeptModel.objects.filter(name=str(get_dept))
    if depts or get_dept == '':
        # return render(request, 'users/add_dept.html')
        return HttpResponse('{"status":"fail","msg":"部门已存在"}', content_type='application/json')
    dept = DeptModel()
    dept.name = get_dept
    dept.save()
    # return render(request, 'index.html')
    return HttpResponse('{"status":"success","msg":"添加成功"}', content_type='application/json')


@login_required
def dept_list(request):
    depts = DeptModel.objects.all().order_by('-id')
    context = {'depts': depts}
    return render(request, 'users/dept_list.html', context)


@login_required
def user_add(request):
    depts = DeptModel.objects.all()
    context = {'depts': depts}
    return render(request, 'users/add_user.html', context)


@login_required
def add_user(request):
    adduser_form = AddUserForm(request.POST)
    if adduser_form.is_valid():
        name = request.POST.get('name', '')
        position = request.POST.get('position', '')
        department = request.POST.get('department', '')
        mobile = request.POST.get('mobile', '')
        work_email = request.POST.get('work_email', '')
        personal_email = request.POST.get('personal_email', '')
        address = request.POST.get('address', '')
        personal_home = request.POST.get('personal_home', '')
        users = UserProfile()
        # depts = DeptModel()
        users.name = name
        users.username = name
        users.position = position
        users.department_id = int(department)
        users.mobile = mobile
        users.work_email = work_email
        users.email = work_email
        users.personal_email = personal_email
        users.address = address
        users.personal_home = personal_home
        users.save()
        return HttpResponse('{"status":"success","msg":"人员信息保存成功"}', content_type='application/json')
    else:
        return HttpResponse('{"status":"fail","msg":"人员信息保存失败"}', content_type='application/json')


@login_required
def user_list(request):
    users = UserProfile.objects.all().order_by('-id')
    context = {'users': users}
    return render(request, 'users/user_list.html', context)


def page_not_found(request):
    from django.shortcuts import render_to_response
    response = render_to_response('error/404.html', {})
    response.status_code = 404
    return response


def page_error(request):
    from django.shortcuts import render_to_response
    response = render_to_response('error/500.html', {})
    response.status_code = 500
    return response