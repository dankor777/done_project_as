# Generated by Django 3.0.6 on 2021-04-13 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projekt_as', '0006_komentarzx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='komentarzx',
            name='reply',
        ),
    ]