# Generated by Django 4.2 on 2023-10-15 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactenquiry', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactenquiry',
            name='last_name',
        ),
    ]
