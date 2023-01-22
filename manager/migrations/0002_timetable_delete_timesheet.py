# Generated by Django 4.1.5 on 2023-01-22 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_subject_alter_teacher_subject'),
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('subject_1', models.ManyToManyField(related_name='subject_1_subject', to='accounts.subject')),
                ('subject_2', models.ManyToManyField(related_name='subject_2_subject', to='accounts.subject')),
                ('subject_3', models.ManyToManyField(related_name='subject_3_subject', to='accounts.subject')),
                ('subject_4', models.ManyToManyField(related_name='subject_4_subject', to='accounts.subject')),
            ],
        ),
        migrations.DeleteModel(
            name='timesheet',
        ),
    ]