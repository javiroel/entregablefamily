from django.shortcuts import render
from  .models import family
from django.http import HttpResponse

# Create your views here.

def family(request):

    family1= family(nombre="Enrique", vinculo="Padre")
    family1.save()
    family2= family(nombre="Lia", vinculo="Amiga")
    family2.save()
    lista_family=[family1,family2]

    return render(request,"Appfamily/Template.html", {"cursos":lista_family})
    return HttpResponse(cadena_Texto)

