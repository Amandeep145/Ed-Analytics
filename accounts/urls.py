from django.urls import path
from .import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name='accounts'
urlpatterns = [
    path('login/',views.login,name="login"),
    path('',views.main_page,name="main_page"),
    path('logout/',views.logout,name="logout"),
    path('lab_menu/', views.lab_menu,name='lab_menu'),
    path('about/',views.about,name="about"),
    path('service/',views.service,name="service"),

]

# urlpatterns += staticfiles_urlpatterns()
