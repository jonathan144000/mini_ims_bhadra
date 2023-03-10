# Generated by Django 4.1.3 on 2022-12-20 05:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fist_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'ims_app_users',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'ims_categories',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('particular', models.TextField(max_length=500)),
                ('ledger_folio', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('total', models.FloatField()),
                ('entry_date', models.DateTimeField(default=datetime.datetime(2022, 12, 20, 11, 20, 15, 301058))),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ims.category')),
            ],
            options={
                'db_table': 'ims_items',
            },
        ),
    ]
