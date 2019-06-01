# Generated by Django 2.1.7 on 2019-02-24 00:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_details', models.TextField()),
                ('change_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('change_made_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='change_log', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DataAPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('version', models.FloatField()),
                ('usage_notes', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('formats_supported', models.CharField(max_length=255)),
                ('managed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_api', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='changelog',
            name='data_api',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data_api.DataAPI'),
        ),
    ]
