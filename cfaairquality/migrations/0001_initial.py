# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-29 08:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor1Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co_data', models.CharField(max_length=50)),
                ('o3_data', models.CharField(max_length=50)),
                ('no2_data', models.CharField(max_length=50)),
                ('pm25_data', models.CharField(max_length=50)),
                ('pm10_data', models.CharField(max_length=50)),
                ('so2_data', models.CharField(max_length=50)),
                ('co_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('o3_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('no2_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('pm25_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('pm10_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('so2_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('pm_nowcast', models.CharField(blank=True, max_length=50, null=True)),
                ('aqi_data', models.CharField(blank=True, max_length=50, null=True)),
                ('log_data', models.CharField(blank=True, max_length=50, null=True)),
                ('lat_data', models.CharField(blank=True, max_length=50, null=True)),
                ('hgt_data', models.CharField(blank=True, max_length=50, null=True)),
                ('tim_data', models.CharField(blank=True, max_length=50, null=True)),
                ('battery_status_data', models.CharField(blank=True, max_length=50, null=True)),
                ('temp_data', models.CharField(blank=True, max_length=50, null=True)),
                ('hum_data', models.CharField(blank=True, max_length=50, null=True)),
                ('data_no', models.IntegerField(default=0)),
                ('data_int', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor2Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co_data', models.CharField(max_length=50)),
                ('o3_data', models.CharField(max_length=50)),
                ('no2_data', models.CharField(max_length=50)),
                ('pm25_data', models.CharField(max_length=50)),
                ('pm10_data', models.CharField(max_length=50)),
                ('so2_data', models.CharField(max_length=50)),
                ('co_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('o3_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('no2_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('pm25_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('pm10_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('so2_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('pm_nowcast', models.CharField(blank=True, max_length=50, null=True)),
                ('aqi_data', models.CharField(blank=True, max_length=50, null=True)),
                ('log_data', models.CharField(blank=True, max_length=50, null=True)),
                ('lat_data', models.CharField(blank=True, max_length=50, null=True)),
                ('hgt_data', models.CharField(blank=True, max_length=50, null=True)),
                ('tim_data', models.CharField(blank=True, max_length=50, null=True)),
                ('battery_status_data', models.CharField(blank=True, max_length=50, null=True)),
                ('temp_data', models.CharField(blank=True, max_length=50, null=True)),
                ('hum_data', models.CharField(blank=True, max_length=50, null=True)),
                ('data_no', models.IntegerField(default=0)),
                ('data_int', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor3Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co_data', models.CharField(max_length=50)),
                ('o3_data', models.CharField(max_length=50)),
                ('no2_data', models.CharField(max_length=50)),
                ('pm25_data', models.CharField(max_length=50)),
                ('pm10_data', models.CharField(max_length=50)),
                ('so2_data', models.CharField(max_length=50)),
                ('co_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('o3_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('no2_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('pm25_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('pm10_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('so2_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('pm_nowcast', models.CharField(blank=True, max_length=50, null=True)),
                ('aqi_data', models.CharField(blank=True, max_length=50, null=True)),
                ('log_data', models.CharField(blank=True, max_length=50, null=True)),
                ('lat_data', models.CharField(blank=True, max_length=50, null=True)),
                ('hgt_data', models.CharField(blank=True, max_length=50, null=True)),
                ('tim_data', models.CharField(blank=True, max_length=50, null=True)),
                ('battery_status_data', models.CharField(blank=True, max_length=50, null=True)),
                ('temp_data', models.CharField(blank=True, max_length=50, null=True)),
                ('hum_data', models.CharField(blank=True, max_length=50, null=True)),
                ('data_no', models.IntegerField(default=0)),
                ('data_int', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor4Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co_data', models.CharField(max_length=50)),
                ('o3_data', models.CharField(max_length=50)),
                ('no2_data', models.CharField(max_length=50)),
                ('pm25_data', models.CharField(max_length=50)),
                ('pm10_data', models.CharField(max_length=50)),
                ('so2_data', models.CharField(max_length=50)),
                ('co_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('o3_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('no2_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('pm25_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('pm10_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('so2_iaqi', models.CharField(blank=True, max_length=50, null=True)),
                ('pm_nowcast', models.CharField(blank=True, max_length=50, null=True)),
                ('aqi_data', models.CharField(blank=True, max_length=50, null=True)),
                ('log_data', models.CharField(blank=True, max_length=50, null=True)),
                ('lat_data', models.CharField(blank=True, max_length=50, null=True)),
                ('hgt_data', models.CharField(blank=True, max_length=50, null=True)),
                ('tim_data', models.CharField(blank=True, max_length=50, null=True)),
                ('battery_status_data', models.CharField(blank=True, max_length=50, null=True)),
                ('temp_data', models.CharField(blank=True, max_length=50, null=True)),
                ('hum_data', models.CharField(blank=True, max_length=50, null=True)),
                ('data_no', models.IntegerField(default=0)),
                ('data_int', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SensorDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_name', models.CharField(max_length=50)),
                ('sensor_city', models.CharField(max_length=50)),
                ('sensor_installed', models.IntegerField(default=0)),
                ('sensor_incare_of', models.CharField(blank=True, max_length=50, null=True)),
                ('sensor_organisation', models.CharField(blank=True, max_length=50, null=True)),
                ('sensor_phoneno', models.CharField(blank=True, max_length=50, null=True)),
                ('sensor_pollutants_var', models.CharField(blank=True, max_length=50, null=True)),
                ('sensor_country', models.CharField(blank=True, max_length=50, null=True)),
                ('sensor_log', models.CharField(blank=True, max_length=50, null=True)),
                ('sensor_lat', models.CharField(blank=True, max_length=50, null=True)),
                ('sensor_height', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='sensor4data',
            name='sensor_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cfaairquality.SensorDetails'),
        ),
        migrations.AddField(
            model_name='sensor3data',
            name='sensor_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cfaairquality.SensorDetails'),
        ),
        migrations.AddField(
            model_name='sensor2data',
            name='sensor_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cfaairquality.SensorDetails'),
        ),
        migrations.AddField(
            model_name='sensor1data',
            name='sensor_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cfaairquality.SensorDetails'),
        ),
    ]
