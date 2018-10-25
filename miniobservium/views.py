from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):

    #Declaramos un diccionario para poder recuperar los objetos recibidos
    datosObjeto = {}

    if(request.method == 'POST'):
        datosObjeto['hostname'] = request.POST.get('hostnameInput', '')
        datosObjeto['version'] = request.POST.get('versionsnmpInput', '')
        datosObjeto['puerto'] = request.POST.get('puertoInput', '')
        datosObjeto['comunidad'] = request.POST.get('comunidadInput', '')
        datosObjeto['nombre'] = request.POST.get('nombreInput', '')

        print(datosObjeto)


    return render(request, 'miniobservium/index.html',{})

# Create your views here.
