# Generated by Django 2.2 on 2019-05-10 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_projects', '0036_auto_20190510_1538'),
        ('notes_and_tasks', '0005_auto_20190211_1645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noteortask',
            options={'ordering': ['-date_and_time_created']},
        ),
        migrations.RemoveField(
            model_name='noteortask',
            name='related_project',
        ),
        migrations.AddField(
            model_name='noteortask',
            name='related_project_output',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data_projects.DataProjectOutput'),
        ),
    ]
