# Generated by Django 2.2 on 2019-05-10 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_projects', '0021_auto_20190321_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataprojectoutput',
            name='current_status',
            field=models.CharField(choices=[('Scoping and preliminary analysis', 'Scoping and preliminary analysis'), ('Awaiting approval to commence draft', 'Awaiting approval to commence draft'), ('Preparing draft', 'Preparing draft'), ('Awaiting internal approval for draft', 'Awaiting internal approval for draft'), ('Submitted to journal or conference', 'Submitted to journal or conference'), ('Accepted', 'Accepted'), ('Completed', 'Completed')], max_length=100),
        ),
    ]
