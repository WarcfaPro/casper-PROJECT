# Generated by Django 4.1.1 on 2022-10-03 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_order_address_street_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='carrier_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='order_carrier', to='main.order_wait_list'),
        ),
    ]
