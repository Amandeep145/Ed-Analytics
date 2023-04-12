from django.db import models

from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey

# Create your models here.


class role_master(models.Model):
    rolename = models.CharField("Role Name",max_length=250)
    rolecode = models.CharField("Role Code",max_length=50)
    roledesc = models.CharField("Role Description",max_length=250)
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        )
    status = models.CharField(max_length=25,choices=STATUS_CHOICES,default='Active')
    created_by = UserForeignKey(auto_user_add=True, verbose_name="The user that is automatically assigned", related_name="role_master_created_by_user")
    updated_by = UserForeignKey(auto_user=True, verbose_name="The user that is automatically assigned", related_name="role_master_updated_by_user")
    
    class Meta:
        db_table = "role_master"
    def __str__(self):
        return "%s " % (self.rolename)



class menu_master1(models.Model):
    menuname = models.CharField("Menu Name",max_length=250)
    menu_parent = models.CharField("Parent Menu",max_length=250)
    menuurl = models.CharField("Menu URL",max_length=50)
    menudesc = models.CharField("Menu Description",max_length=250)
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        )
    status = models.CharField(max_length=25,choices=STATUS_CHOICES,default='Active')
    menu_parent =models.ForeignKey('self', on_delete=models.CASCADE , related_name='parent_menu_master1_fk', default=None, blank=True, null=True)
    created_by = UserForeignKey(auto_user_add=True, verbose_name="The user that is automatically assigned", related_name="menu_master1_created_by_user", null=True)
    updated_by = UserForeignKey(auto_user=True, verbose_name="The user that is automatically assigned", related_name="menu_master1_updated_by_user", null=True)
    iconn = models.CharField("Icon", max_length=50, blank=True, null=True, default = 'fa fa-circle')
   
    class Meta:
        db_table = "menu_master1"
    def __str__(self):
        return "%s " % (self.menuname)     




class role_menu_map(models.Model):
    role_master =models.ForeignKey(role_master, on_delete=models.CASCADE , related_name='role_master_fk', default=None)
    menu_master =models.ForeignKey(menu_master1, on_delete=models.CASCADE , related_name='menu_master_fk', default=None)
    created_by = UserForeignKey(auto_user_add=True, verbose_name="The user that is automatically assigned", related_name="role_menu_map_created_by_user")
    updated_by = UserForeignKey(auto_user=True, verbose_name="The user that is automatically assigned", related_name="role_menu_map_updated_by_user")

    class Meta:
        db_table = "role_menu_map"
        constraints = [models.UniqueConstraint(fields=['role_master','menu_master'], name="role_master_Unique")]
    def __str__(self):
        return "%s " % (self.role_master)



class user_map(models.Model):
    role_master =models.ForeignKey(role_master, on_delete=models.CASCADE , related_name='role1_master_fk', default=None)
    user_master =models.ForeignKey(User, on_delete=models.CASCADE , related_name='user_fk', default=None)
    # lab_master =models.ForeignKey(lab_master, on_delete=models.CASCADE ,blank=True, null=True, related_name='lab_fk', default=None)
    created_by = UserForeignKey(auto_user_add=True, verbose_name="The user that is automatically assigned", related_name="user_map_created_by_user")
    updated_by = UserForeignKey(auto_user=True, verbose_name="The user that is automatically assigned", related_name="user_map_updated_by_user")

    class Meta:
        db_table = "user_map"
        
    def __str__(self):
        return "%s  " % (self.role_master)  

      