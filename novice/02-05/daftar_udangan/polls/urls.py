from django.contrib import admin
from django.urls import path, include

from . import views
from . import forms

urlpatterns = [
    path('',views.home),
    path('tambah/', views.tambah),
    path('hapus/<int:id>',views.hapus),
    path('edit/<int:id>',views.edit),
    # path('admin/', admin.site.urls),
    
]
