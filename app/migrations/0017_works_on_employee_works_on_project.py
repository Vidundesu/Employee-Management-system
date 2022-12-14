# Generated by Django 4.1 on 2022-08-26 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_works_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='works_on',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='works_on',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.project'),
            preserve_default=False,
        ),
    ]
