from django.shortcuts import redirect, render
from django.contrib import auth

# Create your views here.


def login(request):
    if request.method == 'POST':
        username1 = request. POST['lUsername']
        password1 = request. POST['lpassword']

        x = auth.authenticate(username=username1, password=password1)

        if x is not None:
            auth.login(request, x)

            return redirect('home')
        else:

            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def lreg(request):
    return redirect('register page')
