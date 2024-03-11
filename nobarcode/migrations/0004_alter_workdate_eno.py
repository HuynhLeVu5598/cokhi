# Generated by Django 4.2.7 on 2024-01-31 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nobarcode', '0003_workdate_shift'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workdate',
            name='eno',
            field=models.CharField(choices=[('E100', 'Sửa chữa do trở ngại máy'), ('E200', 'Chờ chỉ thị làm việc'), ('E300', 'Chờ linh kiện vật liệu'), ('E400', 'Chỉ đạo huấn luyện - Họp thảo luận'), ('E500', 'Lý do khác'), ('E600', 'Chỉnh lý chỉnh đốn vệ sinh'), ('E700', 'Chào sáng, chào chiều'), ('E800', 'Chuẩn bị công việc'), ('E900', 'Công việc chuẩn bị làm thử')], default='E100', max_length=20),
        ),
    ]
