# Generated by Django 4.1.6 on 2023-02-08 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0006_remove_contract_admin_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='add_extra_days',
            field=models.IntegerField(blank=True, choices=[('5 days', '5 days'), ('10 days', '10 days'), ('25 days', '25 days'), ('50 days', '50 days')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='admin_clients',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='level',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='leverage',
            field=models.IntegerField(blank=True, choices=[('', ''), ('1:100', '1:100'), ('1:200', '1:200'), ('1:500', '1:500'), ('1:1000', '1:1000')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='max_usage_percentage',
            field=models.IntegerField(blank=True, choices=[('35%', '35%'), ('50%', '50%'), ('85%', '85%'), ('100%', '100%')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='time_range',
            field=models.IntegerField(blank=True, choices=[('London ', 'London '), ('Tokyo', 'Tokyo'), ('New York', 'New York')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='trading_timeframe',
            field=models.IntegerField(blank=True, choices=[('1 min', '1 min'), ('5 mins', '5 mins'), ('15 mins', '15 mins'), ('1 hour', '1 hour'), ('1 day', '1 day'), ('all timeframe', 'all timeframe')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contract',
            name='minimum_deposit',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='minimum_duration',
            field=models.IntegerField(blank=True, choices=[('45', '45'), ('60', '60'), ('90', '90')]),
        ),
        migrations.AlterField(
            model_name='contract',
            name='name',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=10),
        ),
    ]
