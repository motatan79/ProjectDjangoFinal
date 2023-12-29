from django.contrib import admin
from .models import RegisteredUser, Pais

# Register your models here.

admin.site.register(Pais)
admin.site.register(RegisteredUser)