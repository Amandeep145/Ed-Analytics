from django.shortcuts import render
from django.http import HttpResponse
from .forms import roleForm, menuForm, SearchContactForm, role_menu_mapForm, user_mapForm
from .models import role_master,menu_master1, role_menu_map, user_map
from django.db import connection
from django.contrib import messages
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
from accounts.decorators import allowed_users
from django.contrib.auth.decorators import login_required



# @login_required
# @allowed_users(allowed_roles=['Admin'])
def menu(request,success=None):
    menu_list =menu_master1.objects.all().values()
    form = SearchContactForm()
    if request.method == 'GET':
        menuname =request.GET.get('menuname')

        if request.GET.get('menuname') == '' :
           
            a = menu_master1.objects.all()
            
        else:
             a = menu_master1.objects.filter(menuname=menuname)
            #  print(a)
    return render(request,'menu_search.html',{'form': form,'ab':a, 'menu_list':menu_list})        



# @login_required
# @allowed_users(allowed_roles=['Admin'])
def menu_add(request, template_name='menu_add.html'):
    status_list = {"Active": "Active", "Inactive": "Inactive"}
    ic = {'Home':'fa fa-home','Teacher':'fa fa-users' ,'Link':'fa fa-link', 'Mail':'fa fa-envelope-o', 'Circle':'fa fa-circle', 'Clock':'fa fa-clock-o', 'User':'fa fa-user', 'Task':'fa fa-tasks', 'Money':'fa fa-money', 'Upload':'fa fa-upload', 'Database':'fa fa-database'}
    # print(ic)
    menu_list =menu_master1.objects.all().values()
    if request.method == 'POST':
        st = request.POST.get('status')
        ico = request.POST.get('icon_name')
        # print(st)
        # print(ico)
        form = menuForm(request.POST, request.FILES) 
        
        if form.is_valid():
            
            menu1= form.cleaned_data['menuname']
            menu2= form.cleaned_data['menuurl']
            menu3= form.cleaned_data['menudesc']
            menu4= form.cleaned_data['status']
            menu5= form.cleaned_data['menu_parent']
            menu6= form.cleaned_data['iconn']
            # print(form.errors)
            if menu_master1.objects.filter(menuname=menu1,menuurl=menu2,menudesc=menu3,status=menu4,menu_parent=menu5, iconn=menu6).exists():
                messages.warning(request,'Menu already exists')
                form = menuForm()
                return render(request, template_name,{'form':form,'status_list':status_list})
            else:
                # messages.warning(request, 'Saved successfully')
                form.save()
                return redirect('rolerights:menu_search')
    else:
        form =menuForm()
        return render(request, template_name, {'form': form,'status_list':status_list,'menu_list':menu_list, 'ic':ic})  



# @login_required
# @allowed_users(allowed_roles=['Admin'])
def menu_edit(request, pk, template_name='menu_edit.html'):
    menu_list =menu_master1.objects.all().values()
    status_list = {"Active": "Active", "Inactive": "Inactive"}
    post = get_object_or_404(menu_master1, pk=pk)
    form = menuForm(request.POST or None, instance=post)
    ic = {'Home':'fa fa-home', 'Link':'fa fa-link', 'Mail':'fa fa-envelope-o', 'Circle':'fa fa-circle', 'Clock':'fa fa-clock-o', 'User':'fa fa-user', 'Task':'fa fa-tasks', 'Money':'fa fa-money', 'Upload':'fa fa-upload', 'Database':'fa fa-database'}
    # print(ic)
    if form.is_valid():
            print('valid')
            me1= form.cleaned_data['menuname']
            me2= form.cleaned_data['menuurl']
            me3= form.cleaned_data['menudesc']
            me4= form.cleaned_data['status']
            me5= form.cleaned_data['menu_parent']
            me6= form.cleaned_data['iconn']
            if menu_master1.objects.filter(menuname=me1,menuurl=me2,menudesc=me3,status=me4,menu_parent=me5, iconn=me6).exists():
                messages.warning(request,'Menu already exists')
                form = menuForm()
                return redirect('rolerights:menu_search')
            else:
                # messages.warning(request, 'Saved successfully')
                form.save()
                return redirect('rolerights:menu_search')
    else:
        form =menuForm(request.POST or None, instance=post)
        return render(request, template_name, {'form': form,'status_list':status_list,'menu_list':menu_list, 'ic':ic})  
    





# @login_required
# @allowed_users(allowed_roles=['Admin'])
def role_search(request,success=None):
    bgg = role_master.objects.all()
    form = SearchContactForm()
    if request.method == 'GET':
        rolename =request.GET.get('rolename')
        if request.GET.get('rolename') == '' :
           
            b = role_master.objects.all()
            
        else:
            b = role_master.objects.filter(rolename = rolename)
            
    return render(request,'role_search.html',{'form': form,'ba':b, 'bgg':bgg})        




# @login_required
# @allowed_users(allowed_roles=['Admin'])
def role_add(request, template_name='role_add.html'):
    status_list = {"Active": "Active", "Inactive": "Inactive"}
    if request.method == 'POST':
        form = roleForm(request.POST, request.FILES ) 
        
        if form.is_valid():
            role1= form.cleaned_data['rolename']
            role2= form.cleaned_data['rolecode']
            role3= form.cleaned_data['roledesc']
            role4= form.cleaned_data['status']
            
            if role_master.objects.filter(rolename=role1,rolecode=role2,roledesc=role3, status=role4).exists():
                messages.warning(request,'Role already exists')
                form = roleForm()
                return render(request, template_name,{'form':form,'status_list':status_list})
            else:
                messages.success(request, 'Saved successfully')
                form.save()
                return redirect('rolerights:role_search')
    else:
        form =roleForm()
        return render(request, template_name, {'form': form,'status_list':status_list})  



# @login_required
# @allowed_users(allowed_roles=['Admin'])
def role_edit(request, pk, template_name='role_edit.html'):
    status_list = {"Active": "Active", "Inactive": "Inactive"}
    post = get_object_or_404(role_master, pk=pk)
    form = roleForm(request.POST or None, instance=post)
    if form.is_valid():
            # print('valid')
            role1= form.cleaned_data['rolename']
            role2= form.cleaned_data['rolecode']
            role3= form.cleaned_data['roledesc']
            role4= form.cleaned_data['status']

            if role_master.objects.filter(rolename=role1,rolecode=role2,roledesc=role3, status= role4).exists():
                messages.warning(request,'Role already exists')
                form = roleForm(request.POST or None, instance=post)
                return redirect('rolerights:role_search')
            else:
                # messages.warning(request, 'Saved successfully')
                success = True
                form.save()
                return redirect('rolerights:role_search')
    else:
        form =roleForm(request.POST or None, instance=post)
        return render(request, template_name, {'form': form,'status_list':status_list})  



# @login_required
# @allowed_users(allowed_roles=['Admin'])
def role_menu_map_add(request,template_name='role_map_add.html'):
    global sub_menu
    role_list =role_master.objects.all().filter(status = 'Active').values()
    menu_list =menu_master1.objects.all().filter(status = 'Active').values()
    main_menu = menu_master1.objects.all().filter(status = 'Active', menuurl = '#').values()
    if 'mainmenu' in request.GET:
        print(request.GET.getlist('menu_master_m'))
        sub_menu = menu_master1.objects.filter(id = request.GET.get('mainmenu'), status = 'Active').values('id')
        # print(sub_menu)
        a = menu_master1.objects.filter(menu_parent_id__in= sub_menu).values_list('menuname','id')
        return JsonResponse(list(a),safe=False)
    # print(main_menu)
    if request.method == 'POST':
        form = role_menu_mapForm(request.POST, request.FILES) 
        su = sub_menu[0]['id']
        # print(su)
        f1= request.POST.get('role_master')
        f2=  request.POST.getlist('menu_master')  
        f2.append(su)
        print(f2)
        for i in f2:    
            if role_menu_map.objects.filter(role_master_id=f1, menu_master_id=i).exists():
                print('heloo')
                messages.warning(request,'Mapping already exists')
                form = role_menu_mapForm()
            else:
                ff = role_menu_map(role_master_id=f1, menu_master_id=i)
                ff.save()
        return redirect('rolerights:role_menu_map_search')
    else:
        form =role_menu_mapForm()
        return render(request, template_name, {'form': form,'role_list':role_list,'menu_list':menu_list, 'main_menu':main_menu})  



# @login_required
# @allowed_users(allowed_roles=['Admin'])
def role_menu_map_search(request,template_name='role_menu_map_search.html'):
    role_list =role_master.objects.all().values()
    form =role_menu_mapForm()
    results =[]
    if 'rolename' in request.GET:
        rolename =request.GET.get('rolename')
        print(rolename)
        if rolename == '':
            act = role_master.objects.all().filter(status = 'Active').values('id')
            # print(act)
            print('hi')
            results = role_menu_map.objects.all().filter(role_master_id__in = act).values('role_master_id__rolename','role_master_id').distinct()
            # print(results)
            r1 = role_menu_map.objects.all().values()
        else:
            act = role_master.objects.all().filter(status = 'Active').values('id')
            results = role_menu_map.objects.all().filter(role_master_id__in = act, role_master_id = rolename).values('role_master_id__rolename','role_master_id').distinct()
            print('hellp')
            print(results)
            # results = role_menu_map.objects.all().values().distinct()
            # results = role_menu_map.objects.all().filter(role_master_id__in = act, role_master_id__rolename = rolename).values('role_master_id__rolename','role_master_id').distinct()
            # results = role_menu_map.objects.filter(role_master=rolename)
    return render(request, template_name, {'form': form,'role_list':role_list,'results':results})  




# @login_required
# @allowed_users(allowed_roles=['Admin'])
def role_menu_map_edit(request, role_master_id):
    roleid = role_master_id
    roles = role_master.objects.all().filter(id = roleid).values()
    r2 = role_menu_map.objects.filter(role_master_id = role_master_id).values('menu_master_id','role_master_id__rolename','role_master_id')
    main_menu = menu_master1.objects.all().filter(status = 'Active', menuurl = '#').values()
    menu_list = role_menu_map.objects.values('id','menu_master_id__menuname','role_master_id', 'menu_master_id')
    # if 'mainmenu' in request.GET:
    #     sub_menu = menu_master1.objects.filter(id = request.GET.get('mainmenu'), status = 'Active').values('id')
    #     # print(sub_menu)
    #     hjj =list( role_menu_map.objects.filter(role_master_id = role_master_id).values_list('menu_master_id__menuname'))
    #     a = list(menu_master1.objects.filter(menu_parent_id__in= sub_menu,).values_list('menuname','id'))
    #     print(hjj)
    #     print(a)
    #     return JsonResponse({'a':a,'hjj':hjj},safe=False)
    hj =list( role_menu_map.objects.filter(role_master_id = role_master_id).values_list('menu_master_id'))
    b =[]
    for  i in range(len(hj)):
        for j in hj[i]:
            b.append(j)
    mk = menu_master1.objects.all().filter(status = 'Active').values()
    print(mk)
    if request.method == "POST":
        ro = request.POST.get('role_master')
        menus = request.POST.getlist('menu_m')
        # print(ro)
        # print(menus)
        al = role_menu_map.objects.filter(role_master_id = ro).values_list('menu_master_id')
        # for i in menus:
        if role_menu_map.objects.filter(role_master_id = ro).exists():
            role_menu_map.objects.all().filter(role_master_id = ro).delete()
            # print('deleted')
            for i in menus:
                zz = role_menu_map(role_master_id = ro, menu_master_id = i )
                zz.save()
                # print(role_menu_map.objects.filter(role_master_id = ro).values())
            return redirect('rolerights:role_menu_map_search')
    return render(request, 'role_menu_map_edit.html', {'menu_list':menu_list, 'roles':roles , 'roleid':roleid ,'r2': r2, 'mk':mk, 'hj':b, 'main_menu':main_menu})


# @login_required
# @allowed_users(allowed_roles=['Admin'])
def user_map_add(request,template_name='user_map_add.html'):
    role_list =role_master.objects.all().filter(status = 'Active').values()
    User_list =User.objects.all().values()
    r = user_map.objects.all().values()
    # print(r)
    if request.method == 'POST':
        form = user_mapForm(request.POST, request.FILES)
        # print(form.errors) 
        
        if form.is_valid():
            
            r1= form.cleaned_data['role_master']
            r2= form.cleaned_data['user_master']
            if user_map.objects.filter(role_master=r1,user_master=r2).exists():
                messages.warning(request,'Mapping already exists')
                form = user_mapForm()
                return render(request, template_name,{'form':form,'role_list':role_list,'User_list':User_list})
            else:
                # messages.warning(request, 'Saved successfully')
                form.save()
                return redirect('rolerights:user_map_search')
    else:
        form =user_mapForm()
        return render(request, template_name, {'form':form,'role_list':role_list,'User_list':User_list})  



# @login_required
# @allowed_users(allowed_roles=['Admin'])
def user_map_search(request,template_name='user_map_search.html'):
    # lab_list =lab_master.objects.all().values()
    use_list =user_map.objects.all().values()
    role_list =role_master.objects.all().values()
    # print(use_list)
    form =user_mapForm()
    results =[]
    if 'rolename' in request.GET:
        form = user_mapForm(request.GET)
        rn =request.GET.get('rolename')
        if rn == '0':
            results = user_map.objects.all()
        else:
            r1 = user_map.objects.all().values()
            ro = request.GET.get('rolename')
            results = user_map.objects.filter(role_master_id = ro)
    return render(request, template_name, {'form': form, 'role_list':role_list, 'results':results})  


# @login_required
# @allowed_users(allowed_roles=['Admin'])
def user_map_edit(request, pk, template_name='user_map_edit.html'):
    role_list =role_master.objects.all().filter(status = 'Active').values()
    User_list =User.objects.all().values()
    post = get_object_or_404(user_map, pk=pk)
    form = user_mapForm(request.POST or None, instance=post)
    if form.is_valid():
        r1= form.cleaned_data['role_master']
        r2= form.cleaned_data['user_master']
        if user_map.objects.filter(role_master=r1,user_master=r2).exists():
            messages.warning(request, 'Mapping exists')
            form = menuForm()
            return render(request, template_name,{'form':form,'role_list':role_list,'User_list':User_list})
        else:
            success = True
            form.save()
            return redirect('rolerights:user_map_search')
    return render(request, template_name, {'form': form,'role_list':role_list,'User_list':User_list})     
    


