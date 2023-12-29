from django.http import HttpResponse

def homepage(request):
    "Para definir la vista en Django"
    return HttpResponse('Welcome to the homepage')