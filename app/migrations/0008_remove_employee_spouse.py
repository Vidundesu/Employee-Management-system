# Generated by Django 4.1 on 2022-08-25 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_department_project_project_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='spouse',
        ),
    ]
