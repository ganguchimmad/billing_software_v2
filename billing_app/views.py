from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .logic_views import account, sub_admin_proccess
from billing_app.models import Users

# Create your views here.
def index(request):
    if request.session.is_empty():
        return render(request,'index.html')
    else:
        return render(request, 'dashboard.html')

#Login process
@csrf_exempt
def login(request):
    return account.login(request)

def logout(request):
    return account.logout(request)

def forgot_password(request):
    return render(request, 'forgot_password.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def shop_details(request):
    return render(request, 'masters/shop_details.html')

def sub_admin(request):
    subadmin_data = Users.objects.all().filter(status=1, user_type = 2)
    front_end_data ={
        "subadmin":subadmin_data
    }
    return render(request, 'masters/sub_admin.html',front_end_data)


    return render(request, 'masters/sub_admin.html')

def add_sub_admin(request):
    return sub_admin_proccess.sub_admin_insert(request)

def shop_keeper(request):
    return render(request, 'masters/shop_keeper.html')

def products(request):
    return render(request, 'masters/products.html')

def brands(request):
    return render(request, 'masters/brands.html')

def sales_report(request):
    return render(request, 'reports/sales_report.html')

def products_report(request):
    return render(request, 'reports/products_report.html')