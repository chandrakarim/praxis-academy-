from django import forms
from django.forms import ModelForm
from django.shortcuts import render, redirect
# from django.core.files.storage import FileSystemStorage
# Create your views here.
from .models import Registrasi
from . import forms
from . import models


# def home(req):
#     return render(req, 'index.html')

def home(req):
    register = Registrasi.objects.all()
    return render(req, 'index.html', {
        'data': register,
    })

def tambah(req):
    choices = Registrasi.CHOICES_VALUE
    multiple_choices = Registrasi.MULTIPLE_CHOICES_VALUE
    if req.POST:
        Registrasi.objects.create(
            no_urut = req.POST['no_urut'],
            nama = req.POST['nama'],
            alamat = req.POST['alamat'],
            jk = req.POST['jk'],
            hobi = req.POST.getlist('hobi'),
            no_tlp = req.POST['no_tlp'],
            img = req.FILES['img'],
            
        )
        return redirect('/polls')
    return render (req, 'polls/tambah.html',{
        'choices' : choices,
        'multiple_choices' : multiple_choices
        })
        
        
    

# def tambah(req):
#     form = forms.FormRegistrasi()
#     if req.POST:
#         form = forms.FormRegistrasi(req.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/polls')
#     return render(req, 'polls/tambah.html',{
#         'form' : form,
#         'choices' : choices
#         # 'multiple_choices' : multiple_choices
#     } )
   

def hapus(req, id):
    dt = Registrasi.objects.get(id=id)
    dt.delete()
    return redirect('/polls')

def edit(req, id):
    data = Registrasi.objects.get(id=id)
    choices = Registrasi.CHOICES_VALUE
    if req.POST:
        Registrasi.objects.filter(pk=id).update(
            nama = req.POST['nama'],
            alamat = req.POST['alamat'],
            jk = req.POST['jk'],
            no_tlp = req.POST['no_tlp'],
        )
        return redirect('/polls')
    return render(req,'polls/edit.html', {
        'choices' : choices,
        'data':data})