# Generated by Django 3.2.4 on 2021-06-30 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_postmodel_postinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='postinfo',
            field=models.TextField(max_length=300, verbose_name='postinfo'),
        ),
    ]
