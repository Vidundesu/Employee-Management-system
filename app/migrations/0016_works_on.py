# Generated by Django 4.1 on 2022-08-26 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_remove_employee_project_project_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Works_on',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DurationField()),
            ],
        ),
    ]