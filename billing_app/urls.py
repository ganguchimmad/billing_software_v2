from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('shop_details', views.shop_details, name='shop_details'),
    path('sub_admin', views.sub_admin, name='sub_admin'),
    path('add_sub_admin', views.add_sub_admin, name='add_sub_admin'),
    path('shop_keeper', views.shop_keeper, name='shop_keeper'),
    path('products', views.products, name='products'),
    path('brands', views.brands, name='brands'),
    path('products_report', views.products_report, name='products_report'),
    path('sales_report', views.sales_report, name='sales_report'),
]