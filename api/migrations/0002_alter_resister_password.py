# Generated by Django 4.1.3 on 2022-11-23 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resister',
            name='password',
            field=models.CharField(max_length=10),
        ),
    ]
