# Generated by Django 5.1.6 on 2025-03-04 00:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_alter_rental_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(help_text='Rating must be between 1 and 5', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
