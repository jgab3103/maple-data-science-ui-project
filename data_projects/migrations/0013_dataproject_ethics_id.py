# Generated by Django 2.1.7 on 2019-03-07 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_projects', '0012_auto_20190307_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataproject',
            name='ethics_id',
            field=models.CharField(default='ETH334433', max_length=255),
            preserve_default=False,
        ),
    ]
