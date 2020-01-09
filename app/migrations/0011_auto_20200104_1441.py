# Generated by Django 3.0.1 on 2020-01-04 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200104_0232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certification',
            old_name='certification_id',
            new_name='identifier',
        ),
        migrations.RemoveField(
            model_name='certification',
            name='technologies',
        ),
        migrations.AddField(
            model_name='technology',
            name='certification',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Certification'),
        ),
    ]