# Generated by Django 4.1 on 2022-08-12 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_employee_skill_alter_department_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.department'),
            preserve_default=False,
        ),
    ]
