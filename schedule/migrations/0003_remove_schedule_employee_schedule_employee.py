# Generated by Django 5.0.6 on 2024-07-03 19:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_availability'),
        ('schedule', '0002_rename_employees_schedule_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='employee',
        ),
        migrations.AddField(
            model_name='schedule',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employees.employee'),
            preserve_default=False,
        ),
    ]