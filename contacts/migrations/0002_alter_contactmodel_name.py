# Generated by Django 3.2.4 on 2021-06-19 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
    ]
