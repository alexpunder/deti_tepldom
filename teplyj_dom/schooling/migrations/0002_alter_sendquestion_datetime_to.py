# Generated by Django 5.0.7 on 2024-07-22 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schooling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendquestion',
            name='datetime_to',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время и дата заявки'),
        ),
    ]
