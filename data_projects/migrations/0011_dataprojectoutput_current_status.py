# Generated by Django 2.1.7 on 2019-02-21 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_projects', '0010_auto_20190221_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataprojectoutput',
            name='current_status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Not yet completed', 'Not yet completed')], default='Completed', max_length=100),
            preserve_default=False,
        ),
    ]
