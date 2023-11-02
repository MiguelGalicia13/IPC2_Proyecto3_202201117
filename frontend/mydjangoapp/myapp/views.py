import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
def myform_view(request):
    if request.method == 'POST':
        data = request.POST.get("data")
        file = request.FILES.get("file")
        if not file:
            return JsonResponse({"message": "No se ha seleccionado un archivo."})
        try:
            # Envía la solicitud al backend de Flask con el archivo adjunto
            files = {"file": (file.name, file.read())}
            if file.name =="mensajes":
                response = requests.post('http://127.0.0.1:5000/grabar_mensaje', data={"data": data}, files=files)
            elif file.name =="configuracion":
                response = requests.post('http://http://127.0.0.1:5000/get_configuracion', data={"data": data}, files=files)
            response.raise_for_status()
            # Procesa la respuesta del backend de Flask
            response_data = response.json()
            return JsonResponse(response_data)
        except requests.exceptions.RequestException as e:
            return HttpResponse(str(e), status=500)
    return render(request, 'myform.html')

def myform_view2(request):
    
    return render(request, 'peticiones.html')

def index(request):
    return render(request, 'index.html')