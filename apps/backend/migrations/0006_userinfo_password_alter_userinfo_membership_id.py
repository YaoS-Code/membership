# Generated by Django 4.2.2 on 2023-06-30 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_memberconsume_consume_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='password',
            field=models.CharField(default='1234', max_length=16, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='membership_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.SET_DEFAULT, to='backend.membership', verbose_name='membership_id'),
        ),
    ]