from django.contrib import admin

# Register your models here.
from .models import role_master, menu_master1, role_menu_map, user_map

# admin.site.register(role_master)
# admin.site.register(menu_master1)
# admin.site.register(role_menu_map)
# admin.site.register(user_map)

@admin.register(role_master)
class roleAdmin(admin.ModelAdmin):
    list_display = ('rolename','rolecode','roledesc' )
    list_filter =  ('rolename','rolecode')
    search_fields =  ('rolename','rolecode')
    ordering = ('rolename','rolecode')

@admin.register(menu_master1)
class menuAdmin(admin.ModelAdmin):
    list_display = ('menuname','menuurl','menudesc','status','menu_parent','iconn' )
    list_filter =  ('menuname','menuurl')
    search_fields =  ('menuname','menuurl')
    ordering = ('menuname','menuurl')

@admin.register(role_menu_map)
class menuAdmin(admin.ModelAdmin):
    list_display= ('role_master','menu_master' )

@admin.register(user_map)
class menuAdmin(admin.ModelAdmin):
    list_display= ('role_master','user_master')    
