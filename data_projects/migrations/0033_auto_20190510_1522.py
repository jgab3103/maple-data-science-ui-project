# Generated by Django 2.2 on 2019-05-10 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_projects', '0032_auto_20190510_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approval',
            name='approval_agency',
            field=models.CharField(choices=[('Aboriginal Health and Medical Research Council of NSW', 'Aboriginal Health and Medical Research Council of NSW'), ('ACT Health Human Research Ethics Committee (HREC)', 'ACT Health Human Research Ethics Committee (HREC)')], max_length=100),
        ),
        migrations.AlterField(
            model_name='approval',
            name='approval_type',
            field=models.CharField(choices=[('Ethics', 'Ethics'), ('Clinician', 'Clinician')], max_length=100),
        ),
    ]
