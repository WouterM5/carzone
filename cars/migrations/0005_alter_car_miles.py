# Generated by Django 4.1.2 on 2022-10-09 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0004_alter_car_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="miles",
            field=models.IntegerField(blank=True),
        ),
    ]
