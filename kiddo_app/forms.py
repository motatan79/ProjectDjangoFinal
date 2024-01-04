from django.forms import ModelForm
from django import forms
from .models import RegisteredUser, Pais, Evento, Tienda

class RegisterForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = RegisteredUser
        fields = '__all__'
        labels = {
            "name": "Nombre",
            "lastname": "Apellido",
            "emailid": "Email Id",
            "telefono": "Teléfono",
            "password": "Password",
            "nacimiento": "Fecha de Nacimiento",
            "pais_origen_id": "País",
            "tienda_id": "Tienda",
            
}


class PaisForm(ModelForm):
    
    class Meta:
        model = Pais
        fields = '__all__'
        labels = {
            "name": "Nombre",
            
} 
        
        
class TiendaForm(ModelForm):
        
    class Meta:
        model = Tienda
        fields = '__all__'
        labels = {
            "nombre": "Nombre",
            "ciudad": "Ciudad",
            "descripcion": "Descripción",
            "tipo_de_tienda": "Tipo Tienda",
    
}
        
class EventoForm(ModelForm):
    
    class Meta:
        model = Evento
        fields = '__all__'
        labels = {
            "patrocinante": "Patrocinante",
            "pais_origen_id": "País",
            "dia_evento": "Día del Evento",
            "tienda_id": "Tienda Patrocinante",
            "gratis": "Gratis",
            "cuota_participacion": "Cuota Participación",    
            
}
