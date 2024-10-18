from django.shortcuts import render
from .models import AlumnoT,Frase
# Create your views here.
def index_vista(request):
    misalumnos=AlumnoT.objects.all().order_by("id")
    return render(request,"index.html",{"misalumnos":misalumnos})