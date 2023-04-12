from django.db import models
# Create your models here.



class Records(models.Model):
    No          = models.IntegerField()
    Name        = models.CharField(max_length = 200 ) 
    Internal    = models.FloatField(max_length = 200) 
    External    = models.FloatField(max_length = 200 ) 
    Subject     = models.CharField(max_length = 200 ) 
    Semester    = models.CharField(max_length = 200 ) 
    Total       = models.FloatField(max_length = 200 ) 

    class Meta:
        ordering = ['Name']

    def __str__(self):
        return f"{self.Name} {self.Subject} {self.Semester} {self.Total}"









# class Teacher(models.Model):
#     teacher_name = models.CharField(max_length = 200)
#     Organisation = models.ForeignKey('Organisation_master', on_delete = models.CASCADE, blank = True, null = True) 

#     class Meta:
#         ordering = ['teacher_name']
    
#     def __str__(self):
#         return f"{self.teacher_name}"





# class Student(models.Model):
#     uid_no = models.CharField(max_length = 200, unique=True)
#     student_name = models.CharField(max_length = 200)
#     Organisation = models.ForeignKey('Organisation_master', on_delete = models.CASCADE, blank = True, null = True) 

#     class Meta:
#         ordering = ['student_name']
    
#     def __str__(self):
#         return f"{self.student_name}"


# class Semesters(models.Model):
#     semester_n = models.CharField(max_length = 200, unique = True)

#     class Meta:
#         ordering = ['semester_n']
    
#     def __str__(self):
#         return f"{self.semester_n}"




# class Subjects(models.Model):
#     subject_n = models.CharField(max_length = 200)
#     standard = models.ForeignKey('Class', on_delete = models.CASCADE, blank = True, null = True)
#     Organisation = models.ForeignKey('Organisation_master', on_delete = models.CASCADE, blank = True, null = True) 
#     # subject_n = models.ForeignKey('Records', on_delete = models.CASCADE, blank = True, null = True)

#     class Meta:
#         ordering = ['subject_n']
    
#     def __str__(self):
#         return f"{self.subject_n} {self.standard}"
    



# class Test(models.Model):
#     test_name = models.CharField(max_length = 200)
#     standard_t = models.ForeignKey('Class', on_delete = models.CASCADE, blank = True, null = True)
#     Organisation = models.ForeignKey('Organisation_master', on_delete = models.CASCADE, blank = True, null = True) 


#     class Meta:
#         ordering = ['test_name']
    
#     def __str__(self):
#         return f"{self.test_name}"



# class Class(models.Model):
#     class_n = models.CharField(max_length = 200)
#     Organisation = models.ForeignKey('Organisation_master', on_delete = models.CASCADE, blank = True, null = True) 

#     class Meta:
#         ordering = ['class_n']
    
#     def __str__(self):
#         return f"{self.class_n}"
    

# class Organisation_master(models.Model):
#     org_name = models.CharField(max_length = 200, unique = True) 

#     class Meta:
#         ordering = ['org_name']
    
#     def __str__(self):
#         return f"{self.org_name}"

# class Marks_Data(models.Model): 
#     Name        = models.ForeignKey('Student', on_delete = models.CASCADE, blank = True, null = True) 
#     Internal    = models.FloatField(max_length = 200, default=0.0) 
#     External    = models.FloatField(max_length = 200 , default=0.0) 
#     Subject     = models.ForeignKey('Subjects', on_delete = models.CASCADE, blank = True, null = True) 
#     Semester    = models.ForeignKey('Semesters', on_delete = models.CASCADE, blank = True, null = True) 
#     Organisation = models.ForeignKey('Organisation_master', on_delete = models.CASCADE, blank = True, null = True) 
#     standard = models.ForeignKey('Class', on_delete = models.CASCADE, blank = True, null = True)
#     test = models.ForeignKey('Test', on_delete = models.CASCADE, blank = True, null = True)
#     Total       = models.FloatField(max_length = 200 ) 

#     class Meta:
#         ordering = ['Name']

#     def __str__(self):
#         return f"{self.Name} {self.Subject} {self.Semester} {self.Total}"

