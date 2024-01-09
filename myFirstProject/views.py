from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    "Para definir la vista en Django"
    return HttpResponse('Welcome to the homepage') 