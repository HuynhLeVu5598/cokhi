# Generated by Django 4.2.7 on 2024-03-08 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nobarcode', '0009_requestinfo_rep_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='v1',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='V1'),
        ),
        migrations.AddField(
            model_name='order',
            name='v2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='V2'),
        ),
    ]
