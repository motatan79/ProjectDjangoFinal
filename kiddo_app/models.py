from django.db import models

# Create your models here.

# Este es el equivalente al Modelo Entidad Relación en SQL (REM)

class Pais(models.Model):
    nombre = models.CharField(max_length = 100)
    
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "País"
        verbose_name_plural = 'Países'


class RegisteredUser(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    nacimiento = models.DateField(null= True, blank = True)
    telefono = models.CharField(blank=True, null=True, max_length=20)
    pais_origen_id = models.ForeignKey(Pais, null = True, blank = True, on_delete = models.SET_NULL, verbose_name = 'País de origen')
    password = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return f'{self.lastname}, {self.name}'
    
