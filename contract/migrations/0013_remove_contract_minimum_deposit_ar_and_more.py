# Generated by Django 4.1.6 on 2023-03-12 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0012_contract_minimum_deposit_ar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='minimum_deposit_ar',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='minimum_deposit_en',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='minimum_duration_ar',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='minimum_duration_en',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='name_ar',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='name_en',
        ),
    ]
