# Generated by Django 2.1.5 on 2019-02-11 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_and_tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noteortask',
            name='type',
            field=models.CharField(choices=[('Note', 'Note'), ('Task', 'Task')], default='Note', max_length=200),
            preserve_default=False,
        ),
    ]
