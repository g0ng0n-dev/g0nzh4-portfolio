# Generated by Django 3.0.1 on 2020-01-04 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200104_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='certification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Certification'),
        ),
    ]