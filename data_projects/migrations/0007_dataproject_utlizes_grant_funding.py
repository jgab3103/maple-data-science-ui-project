# Generated by Django 2.1.7 on 2019-02-21 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_projects', '0006_dataproject_current_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataproject',
            name='utlizes_grant_funding',
            field=models.BooleanField(default=False),
        ),
    ]
