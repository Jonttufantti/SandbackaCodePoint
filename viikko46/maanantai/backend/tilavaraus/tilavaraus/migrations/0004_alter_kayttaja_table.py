# Generated by Django 5.1.3 on 2024-11-15 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tilavaraus', '0003_kayttaja_is_active_kayttaja_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='kayttaja',
            table='kayttaja',
        ),
    ]