from django.conf.urls import url

from operation import views

urlpatterns = [
    url(r'^asset_apply/$', views.asset_apply, name='asset_apply'),
    url(r'^apply_asset/$', views.apply_asset, name='apply_asset'),
    url(r'^apply_list/$', views.apply_list, name='apply_list'),
    url(r'^apply_edit/(?P<apply_id>\d+)/$', views.apply_edit, name='apply_edit'),
    url(r'^edit_apply/(?P<apply_id>\d+)/$', views.edit_apply, name='edit_apply'),
    # url(r'^add_user/$', views.add_user, name='add_user'),
    # url(r'^user_list/$', views.user_list, name='user_list'),
]