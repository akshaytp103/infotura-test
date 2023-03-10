# Generated by Django 4.1.5 on 2023-01-23 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_subject_alter_teacher_subject'),
        ('manager', '0004_remove_timetable_subject_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='subject_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject_1_subject', to='accounts.subject'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject_2_subject', to='accounts.subject'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject_3_subject', to='accounts.subject'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject_4_subject', to='accounts.subject'),
        ),
    ]
