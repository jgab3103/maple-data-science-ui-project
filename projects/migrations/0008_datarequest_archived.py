# Generated by Django 2.2.1 on 2019-05-25 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20190524_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='datarequest',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
