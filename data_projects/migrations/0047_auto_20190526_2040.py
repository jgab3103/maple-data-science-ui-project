# Generated by Django 2.2.1 on 2019-05-26 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_projects', '0046_dataproject_archived'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataprojectoutput',
            name='data_assets',
            field=models.ManyToManyField(blank=True, to='data_assets.DataAsset'),
        ),
    ]
