# Generated by Django 3.2 on 2021-05-01 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartbook',
            options={'verbose_name': 'Cart Book', 'verbose_name_plural': 'Cart Books'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
    ]
