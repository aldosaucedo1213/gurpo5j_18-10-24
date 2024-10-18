from django.contrib import admin
from .models import AlumnoT,Frase
# Register your models here.


class ComentarioIntLine(admin.TabularInline):
    model=Frase
    extra=1

class AlumnoAdmin(admin.ModelAdmin):
    fields=["Apaterno","Amaterno","Nombre","Fecha_Nacimiento","Fecha_Ingreso"]
    list_display=["Apaterno","Amaterno","Nombre"]
    inlines=[ComentarioIntLine]

admin.site.register(AlumnoT,AlumnoAdmin)

@admin.register(Frase)
class FraseAdmin(admin.ModelAdmin):
    fields=["Comentario","Alumno_fk"]
    list_display=["Comentario"]
    



















