# Generated by Django 3.0.8 on 2020-08-07 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inputmodelform',
            name='created_at',
        ),
    ]
