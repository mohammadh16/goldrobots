# Generated by Django 4.1.6 on 2023-02-08 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_account_accountid_alter_account_balance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
    ]