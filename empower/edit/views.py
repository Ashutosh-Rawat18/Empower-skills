#from email.headerregistry import Group
from django.shortcuts import redirect, render
from django.contrib.auth.models import Group

from edit.models import vendors

# Create your views here.


def prof(request):
    return render(request, 'profile.html')


def editprof(request):

    return render(request, 'editprofile.html')


def editprof2(request):
    if request.method == 'POST':
        email = request. POST['email']
        shop_name = request. POST['proShop_name']
        shop_address = request. POST['proShop_address']
        phone_no = request. POST['proShop_number']
        shop_service = request. POST['proShop_service']

        user = Group.objects.create_group(
            email=email, shop_name=shop_name, shop_address=shop_address, phone_no=phone_no, shop_service=shop_service)

        user.save()
        print("user info saved")
        return redirect('edit/prof')
    else:
        return render(request, 'editprofile.html')
