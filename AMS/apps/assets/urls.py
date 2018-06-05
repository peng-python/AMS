from django.conf.urls import url

from assets import views

urlpatterns = [
    url(r'^assets_add/$', views.assets_add, name='assets_add'),
    url(r'^add_assets/$', views.add_assets, name='add_assets'),
    url(r'^first_category/$', views.first_category, name='first_category'),
    url(r'^add_category1/$', views.add_category1, name='add_category1'),
    url(r'^second_category/$', views.second_category, name='second_category'),
    url(r'^add_category2/$', views.add_category2, name='add_category2'),
    # url(r'^get_category1/$', views.get_category1, name='get_category1'),
]