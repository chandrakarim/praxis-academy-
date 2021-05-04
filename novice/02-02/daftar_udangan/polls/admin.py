from django.contrib import admin
from . models import Registrasi 
# Register your models here.
class RegistrationForAdmin(admin.ModelAdmin):
    list_display =['no_urut','nama','alamat','jk','hobi','no_tlp','img']
admin.site.register(Registrasi, RegistrationForAdmin)