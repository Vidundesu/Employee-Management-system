# Generated by Django 4.1 on 2022-08-12 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_employee_project_alter_project_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='spouse',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
