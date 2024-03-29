# Generated by Django 4.2.7 on 2024-01-30 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nobarcode', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('eno', models.CharField(max_length=20)),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('duration_time', models.DurationField()),
                ('note', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_dates', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
