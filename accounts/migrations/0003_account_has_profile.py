# Generated by Django 4.1.5 on 2023-01-21 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_department_user_remove_teacher_useuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='has_profile',
            field=models.BooleanField(default=False),
        ),
    ]
