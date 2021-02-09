# from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


def home_page_view(request):
    return HttpResponse("Hola mundo!")

def otra_prueba(request):
    return HttpResponse("La otra prueba funciona tambien")
