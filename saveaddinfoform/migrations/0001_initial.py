# Generated by Django 4.2 on 2023-10-20 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='saveAddInfoForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_Crime', models.CharField(max_length=30)),
                ('place_of_crime', models.CharField(max_length=40)),
                ('description_of_crime', models.TextField()),
                ('information_of_criminal', models.TextField()),
            ],
        ),
    ]