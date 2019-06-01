# Generated by Django 2.1.5 on 2019-02-11 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes_and_tasks', '0004_auto_20190211_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noteortask',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='noteortask',
            name='related_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data_projects.DataProject'),
        ),
        migrations.AlterField(
            model_name='noteortask',
            name='related_request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.DataRequest'),
        ),
    ]
