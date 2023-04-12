from django.contrib import admin

# Register your models here.
from .models import Records,Semesters,Organisation_master,Class,Marks_Data,Test, Student,Teacher

admin.site.register(Records)
# admin.site.register(Subjectss)
admin.site.register(Semesters)
admin.site.register(Organisation_master)
admin.site.register(Class)
admin.site.register(Marks_Data)
admin.site.register(Test)
admin.site.register(Student)
admin.site.register(Teacher)



