# Generated by Django 4.1.1 on 2022-10-05 11:22

import ckeditor.fields
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.CharField(max_length=100)),
                ('hours', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('payed', models.BooleanField()),
                ('transaction_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('categories', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=8)),
                ('view', models.IntegerField()),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('categories', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=10)),
                ('synopsis', ckeditor.fields.RichTextField()),
                ('download_url', models.TextField()),
                ('image_url', models.TextField()),
            ],
        ),
    ]
