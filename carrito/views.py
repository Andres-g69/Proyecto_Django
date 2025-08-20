from django.shortcuts import render

def carrito_views(request):
    return render(request, 'carrito.html')
