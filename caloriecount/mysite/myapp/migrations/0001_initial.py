# Generated by Django 4.2.18 on 2025-01-18 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('carb', models.FloatField()),
                ('protein', models.FloatField()),
                ('calories', models.IntegerField()),
            ],
        ),
    ]
