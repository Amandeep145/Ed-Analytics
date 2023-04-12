from django.urls import path
from .import views



app_name='dashboard'
urlpatterns = [
    path('dash', views.index, name='dash'),
    path('upload_marks/', views.upload_marks, name='upload_marks'),
    path('studentss/',views.students, name ='student' ),
    path('stud_plot/<pk>',views.stud_plot, name ='stud_plot' ),
    path('only_stud/',views.only_stud, name ='only_stud' ),
    # path('teachers_view/',views.teachers_view, name ='teachers_view' ),
    path('teacher_specific_student/(<str:ak>\d+)/(<str:bk>\d+)$',views.teacher_specific_student, name ='teacher_specific_student' ),
    # path('org_form/', views.org_form, name='org_form'),
    path('Semester_form/', views.Semester_form, name='Semester_form'),
    # path('student_form/', views.student_form, name='student_form'),
    # path('teacher_form/', views.teacher_form, name='teacher_form'),
    # path('subjects_form/', views.subjects_form, name='subjects_form'),
    path('test_form/', views.test_form, name='test_form'),
    # path('class_form/', views.class_form, name='class_form'),
    path('trial_form/',views.trial,name='trial'),
    path('teacher_dynamic/(<str:pk>\d+)/(<str:jk>\d+)$',views.teachers_view_dynamic, name = 'teacher_dynamic')
   

]

