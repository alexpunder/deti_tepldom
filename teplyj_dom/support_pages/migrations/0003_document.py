# Generated by Django 5.0.7 on 2024-07-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support_pages', '0002_ourteam'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('link', models.URLField(verbose_name='Ссылка на документ')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
    ]
