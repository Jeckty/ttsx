from django.contrib import admin
from django.urls import path,re_path
from . import views

app_name='[ttsx]'
urlpatterns = [
    re_path(r'^login/$',views.login,name="login"),
    re_path(r'^cart/$',views.cart,name="cart"),
    re_path(r'^detail/$',views.detail,name="detail"),
    re_path(r'^index/$',views.index,name="index"),
    re_path(r'^list/(\d+)/(\d+)/$',views.list,name="list"),
    re_path(r'^place_order/$',views.place_order,name="place_order"),
    re_path(r'^register/$',views.register,name="register"),
    re_path(r'^user_center_info/$',views.user_center_info,name="user_center_info"),
    re_path(r'^user_center_order/$',views.user_center_order,name="user_center_order"),
    re_path(r'^user_center_site/$',views.user_center_site,name="user_center_site"),
    re_path(r'^checkid/$',views.checkid,name="checkid"),
    re_path(r'^checklogin/$',views.checklogin,name="checklogin"),
    re_path(r'^base/$',views.base,name="base"),
    re_path(r'^quit/$',views.quit,name="quit"),
    re_path(r'^changecart/(\d+)/$',views.changecart,name="changecart"),



]
