# Generated by Django 2.2 on 2021-04-28 05:59

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20210428_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrasi',
            name='hobi',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Membaca', 'Membaca'), ('Berolahraga', 'Berolahraga'), ('Berenang', 'Berenang'), ('Menonton', 'Menonton'), ('Bermain game', 'Bermain game')], default='1', max_length=50),
        ),
    ]
