# Generated by Django 4.1.6 on 2023-02-08 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_account_accountid_alter_account_balance_and_more'),
        ('payment_history', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment_history',
            name='user',
        ),
        migrations.AddField(
            model_name='payment_history',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.account'),
            preserve_default=False,
        ),
    ]
