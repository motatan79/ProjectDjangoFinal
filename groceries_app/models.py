from django.db import models

# Create your models here.

# Este es el equivalente al Modelo Entidad Relación en SQL (REM)

class RegisteredUser(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    phoneNum = models.CharField(blank=True, null=True, max_length=20)
    password = models.CharField(max_length=30)
 
    
