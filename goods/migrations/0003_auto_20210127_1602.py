# Generated by Django 2.2.3 on 2021-01-27 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20210126_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_path',
            field=models.ImageField(upload_to=''),
        ),
    ]