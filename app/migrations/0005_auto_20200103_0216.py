# Generated by Django 3.0.1 on 2020-01-03 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200102_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='url_company',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
