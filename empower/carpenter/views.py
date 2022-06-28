from django.shortcuts import render

# Create your views here.


def car(request):
    return render(request, 'carpenter.html')


def cardc(request):
    return render(request, 'Horizon.html')
