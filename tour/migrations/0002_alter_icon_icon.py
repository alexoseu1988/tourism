# Generated by Django 3.2.13 on 2023-07-20 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icon',
            name='icon',
            field=models.FileField(null=True, upload_to='photos/icons', verbose_name='Иконка'),
        ),
    ]
