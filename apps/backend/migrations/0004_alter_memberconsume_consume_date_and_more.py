# Generated by Django 4.2.2 on 2023-06-28 19:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_consumeitem_membership_credit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberconsume',
            name='consume_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 28, 19, 5, 22, 121154, tzinfo=datetime.timezone.utc), verbose_name='consume_date'),
        ),
        migrations.AlterField(
            model_name='memberpayment',
            name='payment_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 28, 19, 5, 22, 120992, tzinfo=datetime.timezone.utc), verbose_name='payment_date'),
        ),
        migrations.AlterField(
            model_name='servicerecord',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 28, 19, 5, 22, 121444, tzinfo=datetime.timezone.utc), verbose_name='start_date'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 28, 19, 5, 22, 114139, tzinfo=datetime.timezone.utc), verbose_name='register_date'),
        ),
    ]
