# Generated by Django 4.2.9 on 2024-03-03 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='order',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.order'),
        ),
    ]
