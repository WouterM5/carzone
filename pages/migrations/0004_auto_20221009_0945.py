# Generated by Django 3.0.7 on 2022-10-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_teams_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='first_name',
            field=models.CharField(default=None, max_length=255),
        ),
    ]