# Generated by Django 3.2.4 on 2021-06-19 02:40

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
            name='AccountModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50, verbose_name='fullname')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('phone', models.CharField(max_length=100, verbose_name='phone')),
                ('mobile', models.CharField(max_length=100, verbose_name='mobile')),
                ('address', models.CharField(max_length=100, verbose_name='address')),
                ('twitter', models.CharField(max_length=100, verbose_name='twitter')),
                ('instagram', models.CharField(max_length=100, verbose_name='instagram')),
                ('facebook', models.CharField(max_length=100, verbose_name='facebook')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'account',
                'verbose_name_plural': 'accounts',
            },
        ),
    ]
