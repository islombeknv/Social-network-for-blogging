# Generated by Django 3.2.4 on 2021-06-28 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210624_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='updated_at'),
        ),
    ]
