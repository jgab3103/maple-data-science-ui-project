# Generated by Django 2.1.7 on 2019-03-12 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_datarequest_title_or_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='datarequest',
            name='seeking_atsi_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='datarequest',
            name='seeking_clincr_variables',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='datarequest',
            name='seeking_codurf_data',
            field=models.BooleanField(default=False),
        ),
    ]
