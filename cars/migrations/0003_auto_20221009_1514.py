# Generated by Django 3.0.7 on 2022-10-09 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20221009_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
