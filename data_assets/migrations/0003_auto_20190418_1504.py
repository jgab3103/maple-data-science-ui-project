# Generated by Django 2.2 on 2019-04-18 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_assets', '0002_auto_20190321_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataElementAcceptedValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted_value', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='dataelement',
            name='derived_from',
            field=models.ManyToManyField(blank=True, related_name='_dataelement_derived_from_+', to='data_assets.DataElement'),
        ),
        migrations.AddField(
            model_name='dataelement',
            name='null_value_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dataelement',
            name='risk_level',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='DataElementUse',
        ),
        migrations.AddField(
            model_name='dataelementacceptedvalue',
            name='data_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_elements', to='data_assets.DataElement'),
        ),
    ]
