from django.db import models

# Create your models here.

# Este es el equivalente al Modelo Entidad Relación en SQL (REM)

class TipoTienda(models.Model):
    nombre = models.CharField(max_length = 100)
    
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "TipoTienda"
        verbose_name_plural = 'Tipos_Tienda'


class Pais(models.Model):
    nombre = models.CharField(max_length = 100)
    
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "País"
        verbose_name_plural = 'Países'

class Tienda(models.Model):
    nombre = models.CharField(max_length = 100)
    ciudad = models.CharField(max_length = 100)
    descripcion = models.CharField(max_length = 100)
    tipo_de_tienda = models.ForeignKey(TipoTienda, null = True, blank = True, on_delete = models.SET_NULL, verbose_name = 'TipoTienda')
    
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "Tienda"
        verbose_name_plural = 'Tiendas'


class RegisteredUser(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    nacimiento = models.DateField(null= True, blank = True)
    telefono = models.CharField(blank=True, null=True, max_length=20)
    pais_origen_id = models.ForeignKey(Pais, null = True, blank = True, on_delete = models.SET_NULL, verbose_name = 'País de origen')
    tienda_id = models.ForeignKey(Tienda, null = True, blank = True, on_delete = models.SET_NULL, verbose_name = 'Tiendas')
    password = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return f'{self.lastname}, {self.name}'
    
class Evento(models.Model):
    patrocinante = models.ForeignKey(RegisteredUser, null = True, blank = True, on_delete = models.SET_NULL, verbose_name = 'Patrocinante')
    pais_origen_id = models.ForeignKey(Pais, null = True, blank = True, on_delete = models.SET_NULL, verbose_name = 'País de origen')
    dia_evento = models.DateField(null= True, blank = True)
    tienda_id = models.ForeignKey(Tienda, null = True, blank = True, on_delete = models.SET_NULL, verbose_name = 'Tienda')
    gratis = models.BooleanField()
    cuota_participacion = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.patrocinante} - {self.pais_origen_id}'