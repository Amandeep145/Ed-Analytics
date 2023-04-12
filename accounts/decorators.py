from django.http import HttpResponse
from django.shortcuts import redirect
from rolerights.models import role_master, user_map, menu_master1, role_menu_map

# def allowed_users(allowed_roles = []):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#             userid = request.user.id
#             roleid = user_map.objects.filter(user_master=userid).values('role_master')

#             rolename = role_master.objects.filter(id=roleid[0]['role_master']).values('rolename')
#             if rolename[0]['rolename'] in allowed_roles:
                
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return redirect('/dashboard/dash/')
#                 # if rolename[0]['rolename'] == 'Emp':
#                 #     return redirect('/rolerights/user_map_search/')
#         return wrapper_func
#     return decorator
def allowed_users():
    return allowed_users

