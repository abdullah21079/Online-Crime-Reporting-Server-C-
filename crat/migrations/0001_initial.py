# Generated by Django 4.2 on 2023-10-21 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrimeRecordAT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thana_name', models.CharField(max_length=20)),
                ('area_thana', models.FloatField()),
                ('population_thana', models.IntegerField()),
                ('total_street_crime', models.IntegerField()),
                ('crime_rate_per_thousand', models.FloatField()),
                ('density_of_crime_per_sqr_km', models.FloatField()),
            ],
        ),
    ]
