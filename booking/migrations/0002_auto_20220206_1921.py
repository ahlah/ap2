# Generated by Django 3.2.8 on 2022-02-06 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_hotel_rating'),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='description',
        ),
        migrations.AddField(
            model_name='review',
            name='hotel',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='search.hotel'),
        ),
    ]
