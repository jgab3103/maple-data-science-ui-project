# Generated by Django 2.2.1 on 2019-05-25 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_projects', '0043_dataprojectoutput_working_folder'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataproject',
            name='working_folder',
            field=models.CharField(default='To be confirmed', max_length=200),
            preserve_default=False,
        ),
    ]
