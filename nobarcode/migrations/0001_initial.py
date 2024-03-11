# Generated by Django 4.2.7 on 2024-01-26 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeProcessing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stt', models.IntegerField(verbose_name='Số thứ tự')),
                ('execution_time', models.IntegerField(default=0, verbose_name='Thời gian gia công (phút)')),
            ],
        ),
        migrations.CreateModel(
            name='ExcelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='excel_files/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True, verbose_name='Vật liệu')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_s', models.CharField(blank=True, choices=[('Có S chuẩn', 'Có S chuẩn'), ('Sẽ làm S chuẩn', 'Sẽ làm S chuẩn'), ('Không làm S chuẩn', 'Không làm S chuẩn')], max_length=50, null=True, verbose_name='Loại S')),
                ('materials', models.TextField(verbose_name='Vật liệu')),
                ('specification', models.CharField(blank=True, max_length=255, null=True, verbose_name='Quy cách 1 pcs')),
                ('drawing', models.FileField(blank=True, null=True, upload_to='order_drawings/', verbose_name='Bản vẽ PDF')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessingStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_name', models.CharField(max_length=255, verbose_name='Công đoạn')),
            ],
        ),
        migrations.CreateModel(
            name='RequestInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_number', models.CharField(max_length=255, verbose_name='Số yêu cầu')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='Số lượng')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_info', to='nobarcode.order', verbose_name='Mã số thiết bị')),
            ],
        ),
        migrations.CreateModel(
            name='Sno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.TextField(unique=True, verbose_name='S no')),
            ],
        ),
        migrations.CreateModel(
            name='RequestSttProcessing',
            fields=[
                ('request_number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='nobarcode.requestinfo')),
                ('current_stt', models.IntegerField(default=1, verbose_name='Công đoạn hiện tại')),
            ],
        ),
        migrations.CreateModel(
            name='StageTuchu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StageTuchu', models.CharField(max_length=255, verbose_name='Stage Tuchu')),
                ('stt', models.IntegerField(verbose_name='STT')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Employee')),
                ('requirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nobarcode.requestinfo')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessingTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stt', models.IntegerField(verbose_name='Thứ tự công đoạn')),
                ('time_required', models.IntegerField(verbose_name='Thời gian gia công (phút)')),
                ('sno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processing_times', to='nobarcode.sno', verbose_name='Mã số thiết bị')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processing_times', to='nobarcode.processingstage', verbose_name='Công đoạn')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='sno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='nobarcode.sno', verbose_name='Mã số thiết bị'),
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspect', models.CharField(max_length=255, null=True, verbose_name='Inspection')),
                ('max_value', models.FloatField(null=True, verbose_name='Max Value')),
                ('min_value', models.FloatField(null=True, verbose_name='Min Value')),
                ('ok_ng', models.CharField(max_length=5, null=True, verbose_name='OK/NG')),
                ('stt', models.IntegerField(verbose_name='STT')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nobarcode.StageTuchu', verbose_name='Stage')),
            ],
        ),
        migrations.CreateModel(
            name='ExecutionTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.DateTimeField(verbose_name='Start Time')),
                ('time_end', models.DateTimeField(verbose_name='End Time')),
                ('duration', models.IntegerField(default=0, verbose_name='Duration')),
                ('employee_processing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='execution_times', to='nobarcode.employeeprocessing', verbose_name='Employee Processing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='execution_times', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.AddField(
            model_name='employeeprocessing',
            name='request_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_processing', to='nobarcode.requestinfo', verbose_name='Số yêu cầu'),
        ),
        migrations.AddField(
            model_name='employeeprocessing',
            name='sno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_processing', to='nobarcode.sno', verbose_name='Mã số thiết bị'),
        ),
        migrations.AddField(
            model_name='employeeprocessing',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_processing', to='nobarcode.processingstage', verbose_name='Công đoạn'),
        ),
    ]
