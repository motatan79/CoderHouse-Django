from django.http import HttpResponse


def saludo(request) -> HttpResponse:
    return HttpResponse("¡Hola!")

def ingresar_nombre(request) -> HttpResponse:
    nombre = input('Ingresa tu nombre: ')
    return HttpResponse(f'Tu nombre es {nombre}')

def nombre(request, nombre):
    return HttpResponse(nombre)

def fecha_hora(request):
    from datetime import datetime
    ahora = datetime.now()
    return HttpResponse(ahora)

def tirar_dados(request):
    import random
    numero = random.randint(1,6)
    if numero == 6:
        return HttpResponse('Felicitaciones obtuviste el numero 6')
    else: 
        return HttpResponse('Vuelve a intentar')
