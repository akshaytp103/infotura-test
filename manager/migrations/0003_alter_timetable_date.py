# Generated by Django 4.1.5 on 2023-01-22 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_timetable_delete_timesheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='date',
            field=models.DateField(),
        ),
    ]
