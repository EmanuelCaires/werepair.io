# Generated by Django 5.1.4 on 2024-12-28 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category'),
        ),
    ]
