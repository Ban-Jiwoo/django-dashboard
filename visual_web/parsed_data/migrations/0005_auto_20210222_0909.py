# Generated by Django 3.1.6 on 2021-02-22 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0004_auto_20210222_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airchartdb',
            name='dataTime',
            field=models.DateTimeField(null=True),
        ),
    ]
