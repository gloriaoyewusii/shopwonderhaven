# Generated by Django 5.2 on 2025-04-28 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0008_alter_item_seller_id'),
        ('seller', '0004_sellerrepo_sellerservice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='item',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.seller'),
        ),
    ]
