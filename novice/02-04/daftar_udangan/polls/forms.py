from django import forms
from django.forms import ModelForm
from django.shortcuts import render, redirect
# Create your views here.
from .models import Registrasi
class FormRegistrasi(forms.ModelForm):
    class Meta:
        exclude = [ ]
        model = Registrasi

    