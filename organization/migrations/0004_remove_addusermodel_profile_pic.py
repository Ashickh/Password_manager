# Generated by Django 4.0.6 on 2022-09-15 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addusermodel',
            name='profile_pic',
        ),
    ]
