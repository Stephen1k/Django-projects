# Generated by Django 4.2.16 on 2024-11-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_name_order_fname_order_lname'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
    ]
