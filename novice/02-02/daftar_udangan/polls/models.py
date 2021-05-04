from django.db import models

from multiselectfield import MultiSelectField

               
# Create your models here.
class Registrasi(models.Model):
    CHOICES_VALUE = (
        ("Laki-laki", "Laki-laki"),
        ("Perempuan", "Perempuan")
    )
    MULTIPLE_CHOICES_VALUE = (
        ('Membaca', 'Membaca'),
        ('Berolahraga', 'Berolahraga'),
        ('Berenang', 'Berenang'),
        ('Menonton', 'Menonton'),
        ('Bermain game', 'Bermain game')
    )
    no_urut = models.CharField(max_length = 10)
    nama = models.CharField(max_length = 255)
    alamat = models.CharField(max_length = 255)
    jk = models.CharField(max_length = 255, choices = CHOICES_VALUE, blank = True)
    hobi = MultiSelectField(choices = MULTIPLE_CHOICES_VALUE, max_choices=2, default='1')
    no_tlp = models.CharField(max_length = 15)
    img = models.ImageField(upload_to="images/", blank = True, default = '')

    def __str__(self):
        return self.nama