from django.http import HttpResponse
import datetime

def saludo(request):
    return HttpResponse("Hola, Django coder!")

def dia_de_hoy(request):
    dia = datetime.datetime.now()
    documento_de_texto = f"La fecha y hora del día de hoy es la siguiente: {dia}"
    return HttpResponse(documento_de_texto)

def mi_nombre_es(self, nombre):
    documento_de_texto = f"Mi nombre es el siguiente: <br><br>  {nombre}"
    return HttpResponse(documento_de_texto)
