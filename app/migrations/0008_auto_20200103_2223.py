# Generated by Django 3.0.1 on 2020-01-03 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200103_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]