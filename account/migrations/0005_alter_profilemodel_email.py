# Generated by Django 3.2.4 on 2021-06-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210624_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email'),
        ),
    ]
