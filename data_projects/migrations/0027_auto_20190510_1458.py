# Generated by Django 2.2 on 2019-05-10 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_projects', '0026_auto_20190510_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataprojectoutput',
            old_name='pub_med_id',
            new_name='pubmed_id',
        ),
    ]