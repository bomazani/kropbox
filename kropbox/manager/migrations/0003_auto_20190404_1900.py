# Generated by Django 2.2 on 2019-04-04 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20190404_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='folder_type',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]