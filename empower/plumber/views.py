from django.shortcuts import render

# Create your views here.


def plum(request):
    return render(request, 'plumber.html')


def cardc(request):
    return render(request, 'Horizon.html')
