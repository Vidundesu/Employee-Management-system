# Generated by Django 4.1 on 2022-08-25 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_employee_date_of_marriage'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='date_of_marriage',
            field=models.DateField(blank=True, null=True),
        ),
    ]
