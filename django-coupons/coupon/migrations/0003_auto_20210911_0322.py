# Generated by Django 3.1.3 on 2021-09-10 18:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0002_auto_20210910_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='weekday',
            field=models.SmallIntegerField(blank=True, choices=[(0, '월'), (1, '화'), (2, '수'), (3, '목'), (4, '금'), (5, '토'), (6, '일')], null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)], verbose_name='요일'),
        ),
    ]
