from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^add_dept/$', views.add_dept, name='add_dept'),
    url(r'^dept/$', views.dept, name='dept'),
    url(r'^dept_list/$', views.dept_list, name='dept_list'),
    url(r'^user_add/$', views.user_add, name='user_add'),
    url(r'^add_user/$', views.add_user, name='add_user'),
    url(r'^user_list/$', views.user_list, name='user_list'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
]