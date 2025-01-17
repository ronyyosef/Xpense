# Generated by Django 4.0.3 on 2022-04-06 21:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('house_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('public', models.BooleanField(default=False)),
                ('parent_profession_1', models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student'), ('Programmer', 'Programmer'), ('Artist', 'Artist'), ('Manager', 'Manager'), ('Army', 'Army'), ('Police', 'Police'), ('Doctor', 'Doctor'), ('Vet', 'Vet'), ('Nurse', 'Nurse'), ('Technichian', 'Technichian'), ('Cleaner', 'Cleaner'), ('Other', 'Other'), ('Unemployed', 'Unemployed')], default='Other', max_length=50)),
                ('parent_profession_2', models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student'), ('Programmer', 'Programmer'), ('Artist', 'Artist'), ('Manager', 'Manager'), ('Army', 'Army'), ('Police', 'Police'), ('Doctor', 'Doctor'), ('Vet', 'Vet'), ('Nurse', 'Nurse'), ('Technichian', 'Technichian'), ('Cleaner', 'Cleaner'), ('Other', 'Other'), ('Unemployed', 'Unemployed')], default='Other', max_length=50)),
                ('income', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('children', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.TextField(default='', max_length=250)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='house.city')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='house.country')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.country'),
        ),
    ]
