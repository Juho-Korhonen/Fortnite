# Generated by Django 4.0.3 on 2022-06-19 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('medications', models.CharField(max_length=10000)),
                ('emergency_number', models.CharField(blank=True, max_length=20)),
                ('extra_info', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('inside_facility', models.BooleanField(default=False)),
            ],
        ),
    ]
