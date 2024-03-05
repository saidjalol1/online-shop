# Generated by Django 4.2.9 on 2024-03-05 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_order_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode_image', models.ImageField(upload_to='barcodes/')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.order')),
            ],
        ),
    ]
