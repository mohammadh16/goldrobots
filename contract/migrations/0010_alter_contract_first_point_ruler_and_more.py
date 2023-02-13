# Generated by Django 4.1.6 on 2023-02-13 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0009_contract_first_point_ruler_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='first_point_ruler',
            field=models.IntegerField(blank=True, default=5),
        ),
        migrations.AlterField(
            model_name='contract',
            name='fourth_point_ruler',
            field=models.IntegerField(blank=True, default=20),
        ),
        migrations.AlterField(
            model_name='contract',
            name='second_point_ruler',
            field=models.IntegerField(blank=True, default=10),
        ),
        migrations.AlterField(
            model_name='contract',
            name='third_point_ruler',
            field=models.IntegerField(blank=True, default=15),
        ),
    ]