# Generated by Django 5.1.3 on 2024-12-11 04:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(blank=True, max_length=255, null=True)),
                ('doc_spec', models.CharField(blank=True, max_length=255, null=True)),
                ('doc_image', models.ImageField(blank=True, null=True, upload_to='doctors')),
                ('dep_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.departments')),
            ],
        ),
    ]