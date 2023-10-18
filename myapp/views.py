from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola, mundo. Estás en la página de inicio de mi aplicación.")

def login_view(request):
   return render(request, 'login.html')


