# Generated by Django 2.1.7 on 2019-02-21 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_projects', '0007_dataproject_utlizes_grant_funding'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataprojectoutput',
            name='output_title_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
