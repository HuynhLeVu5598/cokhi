# Generated by Django 4.2.7 on 2024-02-21 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nobarcode', '0007_alter_workdate_duration_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='executiontime',
            name='num_machine',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='executiontime',
            name='shift',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
