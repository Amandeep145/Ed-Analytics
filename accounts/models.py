from django.db import models

# Create your models here.




class Contact(models.Model):
    Name        = models.CharField(max_length = 200, blank = True, null = True) 
    Email       = models.EmailField(max_length= 254, blank = True, null = True)
    Subject     = models.CharField(max_length = 200, blank = True, null = True) 
    Message     = models.TextField(max_length = 400, blank = True, null = True) 

    class Meta:
        ordering = ['Name']

    def __str__(self):
        return f"{self.Name} {self.Email} {self.Subject} {self.Message}"
