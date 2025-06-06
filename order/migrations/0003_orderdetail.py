# Generated by Django 4.2.6 on 2023-11-25 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('order', '0002_alter_order_customer_alter_order_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_price', models.IntegerField(blank=True, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('current_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_order', to='order.order')),
                ('current_products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_products', to='products.products')),
            ],
        ),
    ]
