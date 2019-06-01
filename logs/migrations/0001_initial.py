# Generated by Django 2.1.5 on 2019-02-11 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataUploadLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('OK', 'OK'), ('Fail', 'Fail'), ('Landed', 'Landed'), ('Staged', 'Staged')], max_length=50)),
            ],
        ),
    ]
