# Generated by Django 4.1.6 on 2023-02-08 10:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='leverage',
            field=models.CharField(choices=[('1:100', '1:100'), ('1:200', '1:200'), ('1:500', '1:500'), ('1:1000', '1:1000')], default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='trading_timeframe',
            field=models.CharField(choices=[('1 min', '1 min'), ('5 min', '5 min'), ('15 min', '15 min'), ('D', 'D')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contract',
            name='admin_client',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='garantie_percentage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='minimum_deposit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='minimum_duration',
            field=models.IntegerField(),
        ),
    ]