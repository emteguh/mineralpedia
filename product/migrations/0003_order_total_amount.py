# Generated by Django 4.2 on 2023-06-04 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_order_alter_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="total_amount",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
