# Generated by Django 2.2 on 2021-04-29 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_registrasi_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrasi',
            name='img',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
