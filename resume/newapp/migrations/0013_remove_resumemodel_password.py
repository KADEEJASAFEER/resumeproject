# Generated by Django 3.1 on 2020-10-10 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0012_auto_20201010_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resumemodel',
            name='password',
        ),
    ]
