# Generated by Django 5.2 on 2025-04-30 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0012_rename_seller_item_seller_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
