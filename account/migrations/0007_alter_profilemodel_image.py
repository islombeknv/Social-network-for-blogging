# Generated by Django 3.2.4 on 2021-06-25 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_profilemodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='image'),
        ),
    ]
