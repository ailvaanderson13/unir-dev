# Generated by Django 3.1.7 on 2021-02-25 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210225_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='reset_password',
            field=models.BooleanField(default=False),
        ),
    ]
