# Generated by Django 4.1.1 on 2022-10-04 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_order_carrier_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='carrier_id',
        ),
        migrations.RemoveField(
            model_name='order_wait_list',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='carrier',
            field=models.ManyToManyField(to='main.order_wait_list'),
        ),
        migrations.AddField(
            model_name='order_wait_list',
            name='order_in_w_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_in_list', to='main.order', verbose_name='Заказ'),
        ),
    ]
