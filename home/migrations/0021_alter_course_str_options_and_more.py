# Generated by Django 4.0.4 on 2022-05-22 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_live_bool_live_latitude_live_longitude_live_radius'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course_str',
            options={'ordering': ('time_present',)},
        ),
        migrations.AlterModelOptions(
            name='student_attendace_report',
            options={'ordering': ('time_present',)},
        ),
    ]
