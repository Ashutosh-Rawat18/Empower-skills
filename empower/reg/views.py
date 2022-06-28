
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.


def sign(request):
    if request.method == 'POST':
        username = request. POST['cUsername']
        first_name = request. POST['cFirst_name']
        last_name = request. POST['clast_name']
        email = request. POST['cEmail_ID']
        password = request. POST['cPassword']

        user = User.objects.create_user(
            username=username, first_name=first_name, last_name=last_name, email=email, password=password)

        user.save()
        print("user created")
        return redirect('/')

    else:
        return render(request, 'register.html')

# return render(request, 'register.html')
