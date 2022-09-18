# Generated by Django 4.1.1 on 2022-09-18 20:16

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
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_city', models.CharField(max_length=50)),
                ('address_street', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('is_complete', models.BooleanField(default=False)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('data_complete', models.DateTimeField(auto_now=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
