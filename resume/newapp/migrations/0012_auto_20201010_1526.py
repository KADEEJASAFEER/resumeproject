# Generated by Django 3.1 on 2020-10-10 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0011_auto_20201010_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resumemodel',
            old_name='lastdegree',
            new_name='qualification',
        ),
    ]