# Generated by Django 3.0.1 on 2020-01-03 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200103_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='url_project',
            field=models.URLField(null=True),
        ),
    ]
