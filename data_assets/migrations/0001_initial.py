# Generated by Django 2.1.5 on 2019-02-11 04:58

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
            name='DataAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owning_org', models.CharField(max_length=200)),
                ('owning_business_unit', models.CharField(choices=[('Strategic Research and Investment', 'Strategic Research and Investment'), ('Cancer Services and Information', 'Cancer Services and Information'), ('Cancer Screening and Prevention', 'Cancer Screening and Prevention'), ('CI-IT', 'CI-IT'), ('CI-Admin', 'CI-Admin'), ('Other', 'Other')], max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('asset_id', models.CharField(max_length=200)),
                ('version', models.DecimalField(decimal_places=3, max_digits=10)),
                ('type', models.CharField(choices=[('System', 'System'), ('Extract', 'Extract'), ('Analytics', 'Analytics'), ('Reporting', 'Reporting'), ('Auxiliary', 'Auxiliary'), ('Sample', 'Sample')], max_length=200)),
                ('emergency_shutdown_contact', models.CharField(max_length=200)),
                ('emergency_shutdown_org', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('data_limiting_marker', models.CharField(choices=[('For Official Use Only', 'For Official Use Only'), ('Sensitive - Personal', 'Sensitive - Personal'), ('Sensitive - Health Information', 'Sensitive - Health Information'), ('Senstitive - Legal', 'Senstitive - Legal'), ('Senstitive - NSW Government', 'Senstitive - NSW Government'), ('Senstitive - NSW Cabinet', 'Senstitive - NSW Cabinet')], max_length=200)),
                ('update_frequency', models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Annually', 'Annually'), ('Ad-hoc', 'Ad-hoc')], max_length=200)),
                ('currently_active', models.BooleanField(default=False)),
                ('utlizes_external_data', models.BooleanField(default=False)),
                ('governed_as_external_data', models.BooleanField(default=False)),
                ('available_for_analytics', models.BooleanField(default=False)),
                ('under_review', models.BooleanField(default=False)),
                ('used_in_shared_dictionary', models.BooleanField(default=False)),
                ('usage_notes', models.TextField()),
                ('data_location_type', models.CharField(choices=[('Web Resource', 'Web Resource'), ('Internal Server', 'Internal Server'), ('External Server', 'External Server')], max_length=200)),
                ('data_location', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('supporting_documentation', models.CharField(max_length=255)),
                ('related_asset', models.ManyToManyField(blank=True, related_name='_dataasset_related_asset_+', to='data_assets.DataAsset')),
            ],
            options={
                'verbose_name_plural': 'Data assets',
            },
        ),
        migrations.CreateModel(
            name='DataAssetBreach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_report', models.DateField(default=datetime.datetime.now)),
                ('summary', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('related_documentation', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Data asset breaches',
            },
        ),
        migrations.CreateModel(
            name='DataAssetRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Data Sponsor', 'Data Sponsor'), ('Data Custodian', 'Data Custodian'), ('Data Stewart', 'Data Stewart'), ('Data User', 'Data User'), ('Business Owner', 'Business Owner'), ('System Owner', 'System Owner'), ('System User', 'System User')], max_length=100)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=100)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('data_asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_assets.DataAsset')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DataElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('name_is_conformed', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=200)),
                ('definition', models.TextField()),
                ('accepted_values', models.TextField()),
                ('legacy_collection', models.CharField(default='unknown', max_length=255)),
                ('category', models.CharField(choices=[('Person', 'Person'), ('Case', 'Case'), ('Episode', 'Episode'), ('Health Practitioner', 'Health Practitioner'), ('Health Organisation', 'Health Organisation'), ('Grant', 'Grant'), ('Clinical Trial', 'Clinical Trial')], max_length=255)),
                ('usage_notes', models.TextField()),
                ('under_review', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DataElementUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_element_name', models.CharField(max_length=100, null=True)),
                ('destination_element_name', models.CharField(max_length=100, null=True)),
                ('destination_name_is_conformed', models.BooleanField(default=False)),
                ('element_use_id', models.CharField(max_length=50)),
                ('risk_level', models.IntegerField()),
                ('null_value_accepted', models.BooleanField(default=False)),
                ('destination_asset_usage_notes', models.TextField()),
                ('element_transformation_rules', models.TextField()),
                ('under_review', models.BooleanField(default=False)),
                ('data_element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_elements', to='data_assets.DataElement')),
                ('destination_data_asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_element_destination', to='data_assets.DataAsset')),
                ('source_data_asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_element_source', to='data_assets.DataAsset')),
            ],
        ),
    ]
