# Generated by Django 5.1.4 on 2024-12-17 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_remove_product_x'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
