# Generated by Django 2.1.7 on 2019-02-21 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_projects', '0004_auto_20190221_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataprojectinvestigator',
            name='role',
            field=models.CharField(choices=[('Lead investigator', 'Lead investigator'), ('Investigator', 'Investigator'), ('Co-investigator', 'Co-investigator')], default='Investigator', max_length=255),
            preserve_default=False,
        ),
    ]
