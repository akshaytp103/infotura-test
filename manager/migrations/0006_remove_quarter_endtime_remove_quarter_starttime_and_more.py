# Generated by Django 4.1.5 on 2023-01-23 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_subject_alter_teacher_subject'),
        ('manager', '0005_alter_timetable_subject_1_alter_timetable_subject_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quarter',
            name='endtime',
        ),
        migrations.RemoveField(
            model_name='quarter',
            name='starttime',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='subject_1',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='subject_2',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='subject_3',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='subject_4',
        ),
        migrations.AddField(
            model_name='timetable',
            name='quarter_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quarter_1_quarter', to='manager.quarter'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='quarter_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quarter_2_quarter', to='manager.quarter'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='quarter_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quarter_3_quarter', to='manager.quarter'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='quarter_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quarter_4_quarter', to='manager.quarter'),
        ),
        migrations.CreateModel(
            name='Subject_Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('subject_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject_1_subject', to='accounts.subject')),
                ('subject_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject_2_subject', to='accounts.subject')),
                ('subject_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject_3_subject', to='accounts.subject')),
                ('subject_4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject_4_subject', to='accounts.subject')),
            ],
        ),
    ]
