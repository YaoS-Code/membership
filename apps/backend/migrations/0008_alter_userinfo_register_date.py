# Generated by Django 4.2.2 on 2023-06-30 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_alter_userinfo_dob_alter_userinfo_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='register_date',
            field=models.DateField(blank=True, null=True, verbose_name='register_date'),
        ),
    ]