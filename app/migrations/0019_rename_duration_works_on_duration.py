# Generated by Django 4.1 on 2022-08-26 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_works_on_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='works_on',
            old_name='duration',
            new_name='Duration',
        ),
    ]
