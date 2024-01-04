from django.contrib import admin
from .models import RegisteredUser, Pais, TipoTienda, Evento, Tienda

# Register your models here.

admin.site.register(TipoTienda)
admin.site.register(Tienda)
admin.site.register(Pais)
admin.site.register(RegisteredUser)
admin.site.register(Evento)
