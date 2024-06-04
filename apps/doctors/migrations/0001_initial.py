# Generated by Django 4.2.7 on 2024-06-02 23:34

import uuid

import django.db.models.deletion
import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cabinets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30, verbose_name='Firstname')),
                ('last_name', models.CharField(max_length=30, verbose_name='Lastname')),
                ('father_name', models.CharField(blank=True, max_length=30, verbose_name='Fathername')),
                ('cabinets', models.ManyToManyField(blank=True, related_name='doctors', to='cabinets.cabinet', verbose_name='Cabinet')),
                ('priority_cabinet', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='priority_doctors', to='cabinets.cabinet', verbose_name='Priority cabinet')),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctors',
            },
        ),
    ]
