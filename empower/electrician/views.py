from django.shortcuts import render

# Create your views here.


def elec(request):
    return render(request, 'electrician.html')


def cardc(request):
    return render(request, 'Horizon.html')
