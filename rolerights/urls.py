from django.urls import path
from .import views
from django.conf.urls import url


app_name='rolerights'
urlpatterns = [
    path('menu/', views.menu, name='menu_search'),
    path('menu_add/', views.menu_add, name='menu_add'),
    path('menu_edit/<pk>', views.menu_edit, name='menu_edit'),
    path('role_add/', views.role_add, name = 'role_add'),
    path('role_search/', views.role_search, name='role_search'),
    path('role_edit/<pk>', views.role_edit, name = 'role_edit'),
    path('role_menu_map/', views.role_menu_map_add, name='role_menu_map'),
    path('role_menu_map_edit/<role_master_id>', views.role_menu_map_edit, name='role_menu_map_edit'),
    path('role_menu_map_search/', views.role_menu_map_search, name='role_menu_map_search'),
    path('user_map/', views.user_map_add, name='user_map_add'),
    path('user_map_edit/<pk>', views.user_map_edit, name='user_map_edit'),
    path('user_map_search/', views.user_map_search, name='user_map_search'),
     
]