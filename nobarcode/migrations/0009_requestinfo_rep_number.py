# Generated by Django 4.2.7 on 2024-03-05 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nobarcode', '0008_executiontime_num_machine_executiontime_shift'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestinfo',
            name='rep_number',
            field=models.IntegerField(default=0, verbose_name='Số rep'),
            preserve_default=False,
        ),
    ]