from django import forms
from django.forms import ModelForm
from django.shortcuts import render, redirect
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
    if req.POST:
        Registrasi.objects.create(
            no_urut = req.POST['no_urut'],
            nama = req.POST['nama'],
            alamat = req.POST['alamat'],
            no_tlp = req.POST['no_tlp'],
        )
        return redirect('/')
    return render (req, 'tambah.html')

def tambah(req):
    form = forms.FormRegistrasi()
    if req.POST:
        form = forms.FormRegistrasi(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/polls')
    return render(req, 'polls/tambah.html',{
        'form' : form,
    } )

def hapus(req, id):
    dt = Registrasi.objects.get(id=id)
    dt.delete()
    return redirect('/polls')

def edit(req, id):
    data = Registrasi.objects.get(id=id)
    if req.POST:
        Registrasi.objects.filter(pk=id).update(
            nama = req.POST['nama'],
            alamat = req.POST['alamat'],
            no_tlp = req.POST['no_tlp'],
        )
        return redirect('/polls')
    return render(req,'polls/edit.html', {'data':data})