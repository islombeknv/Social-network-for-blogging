# Generated by Django 3.2.4 on 2021-06-24 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=150, verbose_name='fullname')),
                ('phone', models.IntegerField(max_length=50, verbose_name='phone')),
                ('position', models.CharField(max_length=100, verbose_name='position')),
                ('address', models.CharField(max_length=250, verbose_name='address')),
                ('twitter', models.CharField(max_length=60, verbose_name='twitter')),
                ('instagram', models.CharField(max_length=60, verbose_name='instagram')),
                ('facebook', models.CharField(max_length=60, verbose_name='facebook')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated_at')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'userprofile',
                'verbose_name_plural': 'userprofile',
            },
        ),
    ]
