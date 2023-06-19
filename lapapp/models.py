from django.db import models


from datetime import datetime

# Create your models here.

class addUser(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    email=models.EmailField(max_length=30)

    def __str__(self) :
         return self.username
    

class Contact(models.Model):
     name=models.CharField(max_length=20)
     email=models.EmailField(max_length=30)
     message=models.CharField(max_length=60)

     created_at=models.DateTimeField(default=datetime.now())
     resolved_at=models.BooleanField(default=False)

     def __str__(self):
          return self.name


