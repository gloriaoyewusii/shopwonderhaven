# Generated by Django 5.2 on 2025-04-30 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0013_alter_item_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='seller_id',
            new_name='seller',
        ),
    ]
