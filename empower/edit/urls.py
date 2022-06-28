from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('prof', views.prof, name='prof'),
    path('editprof2', views.editprof2, name='editprof2'),
    # path('editprof', views.editprof, name='editprof'),
]
