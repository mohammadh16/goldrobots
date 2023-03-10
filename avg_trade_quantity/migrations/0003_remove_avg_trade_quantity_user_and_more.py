# Generated by Django 4.1.6 on 2023-02-08 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_account_accountid_alter_account_balance_and_more'),
        ('avg_trade_quantity', '0002_alter_avg_trade_quantity_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avg_trade_quantity',
            name='user',
        ),
        migrations.AddField(
            model_name='avg_trade_quantity',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.account'),
            preserve_default=False,
        ),
    ]
