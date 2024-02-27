# Generated by Django 4.2.9 on 2024-02-26 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nomi')),
                ('slug', models.SlugField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nomi')),
                ('image', models.ImageField(null=True, upload_to='mahsulotlar/')),
                ('amount', models.CharField(max_length=100, verbose_name='Miqdori')),
                ('price', models.PositiveBigIntegerField(default=0, verbose_name='Narxi')),
                ('description', models.CharField(max_length=300, verbose_name='Tavsifi')),
                ('discount', models.PositiveIntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan_sanasi")),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category', verbose_name='kategoriyasi')),
            ],
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=0, verbose_name='Miqdori')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Mahsulot')),
            ],
        ),
    ]