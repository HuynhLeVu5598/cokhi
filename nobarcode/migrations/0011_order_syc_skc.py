# Generated by Django 4.2.7 on 2024-03-09 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nobarcode', '0010_order_v1_order_v2'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='syc_skc',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Số yêu cầu'),
        ),
    ]
