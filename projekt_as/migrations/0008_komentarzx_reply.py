# Generated by Django 3.0.6 on 2021-04-14 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projekt_as', '0007_remove_komentarzx_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='komentarzx',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='projekt_as.KomentarzX'),
        ),
    ]