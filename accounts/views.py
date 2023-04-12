from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import pandas as pd 
from django.db.models import Sum
import plotly.express as px
from django.db import connection
from django.contrib.auth.models import User,Group
from rolerights.models import role_master, menu_master1, role_menu_map, user_map
import json
from django.http import JsonResponse
import numpy as np


  
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def login(request):
#     if request.method =='POST':
#         user= auth.authenticate(username=request.POST['username'],password=request.POST['password'])
      
#         if user is not None:
#             auth.login(request,user)
#             if  request.user.is_active:
#                 return redirect('dashboard:dash')
#         else:
#             messages.error(request,'User Name or Password is Incorrect')
#             return redirect('accounts:login')  
    
#     else:
#         return render(request, 'login.html')
    


from .models import Contact
    
def main_page(request):
    if request.method == 'POST':
        name =request.POST.get('na')
        email =request.POST.get('em')
        subject =request.POST.get('su')
        message =request.POST.get('me')
        print(name)
        if Contact.objects.filter(Name = name, Email = email, Subject = subject, Message = message).exists():
            pass
        else:
            z = Contact(Name = name, Email = email, Subject = subject, Message = message)
            z.save()
        return render(request, 'index1.html')
    return render(request, 'index1.html')

def about(request):
    return render(request, 'about.html')
def service(request):
    return render(request, 'service.html')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.method =='POST':
        user= auth.authenticate(username=request.POST['username'],password=request.POST['password'])
      
        if user is not None:
            auth.login(request,user)
            if  request.user.is_active:
                userid = request.user.id
                roleid = user_map.objects.filter(user_master=userid).values('role_master')
                allowed_roles = ['Student']
                rolename = role_master.objects.filter(id=roleid[0]['role_master']).values('rolename')
                if rolename[0]['rolename'] == 'Student':
                    print(rolename[0]['rolename'])
                    return redirect('dashboard:only_stud')
                elif rolename[0]['rolename'] == 'Teacher':
                    a = 'CA'
                    b = 'SEM_I'
                    return redirect('dashboard:teacher_dynamic',pk=a,jk=b)
                else:
                     return redirect('dashboard:dash')
        else:
            messages.error(request,'User Name or Password is Incorrect')
            return redirect('accounts:login')  
    
    else:
        return render(request, 'alt_login.html')





  
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def logout(request):
    auth.logout(request)
    return redirect('accounts:login') 


@login_required
def lab_menu(request):
    ui = request.user.id
    ro = user_map.objects.filter(user_master_id = ui).values_list('role_master_id',flat=True)
    # print(ro)
    ro1 = user_map.objects.all().values()
    rmid = list(ro)
    mo = role_menu_map.objects.filter(role_master_id = rmid[0]).values_list('menu_master_id',flat=True)

    # result_data = menu_master1.objects.filter(id__in =  mo).values()    
    # print(result_data)
    result_data = menu_master1.objects.filter(id__in =  mo, status = 'Active').values()  
    result_data1 = menu_master1.objects.all().values()    
    # print(result_data1)
    dff = pd.DataFrame(list(result_data1),columns=['id','menu_parent_id','menuname','menuurl','iconn'])
    df = pd.DataFrame(list(result_data),columns=['id','menu_parent_id','menuname','menuurl','iconn'])
    df['depth'] = np.where(df['menuurl'] == '#', 1, 2)
    df = df.sort_values(by=['depth'])
    # print(df)
    return JsonResponse(json.dumps(df.to_dict(orient='records')),safe=False)
