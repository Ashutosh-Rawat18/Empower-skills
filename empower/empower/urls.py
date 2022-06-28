"""empower URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path, include
from carpenter.views import cardc
from log.views import login
from log.views import logout
from reg.views import sign
from edit.views import editprof
from log.views import lreg


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('reg/', include('reg.urls')),
    #path('log/', include('log.urls')),
    path('login/', login, name='login'),
    path('login/reg/', sign, include('reg.urls')),
    path('logout', logout, name="logout"),
    path('edit/', include('edit.urls')),
    path('editprof', editprof, name="editprof"),
    path('reg', lreg, name="lreg"),
    path('carpenter/', include('carpenter.urls')),
    path('cardc', cardc, name="cardc"),
    path('plumber/', include('plumber.urls')),
    path('electrician/', include('electrician.urls')),


]
