# Generated by Django 4.2.9 on 2024-03-06 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_order_payment_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold_amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
