# Generated by Django 4.1.6 on 2023-02-07 20:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0003_employee_photo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountid', models.IntegerField()),
                ('phone', models.CharField(max_length=20)),
                ('registration_date', models.DateField(default=datetime.datetime.now)),
                ('email', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('total_balance', models.IntegerField()),
                ('total_profit', models.IntegerField()),
                ('total_trades', models.IntegerField()),
                ('new_trades', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('remaining_days', models.IntegerField()),
                ('leverage', models.CharField(max_length=10)),
                ('percentage_in_trade', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employee.employee')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
