# Generated by Django 2.1.7 on 2019-03-06 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_projects', '0011_dataprojectoutput_current_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataprojectgrantapplicationreviewerscore',
            name='reviewer_name',
            field=models.CharField(default='Bob smith', max_length=255),
            preserve_default=False,
        ),
    ]
