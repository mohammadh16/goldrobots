# Generated by Django 4.1.6 on 2023-02-06 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_remove_employee_account_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
