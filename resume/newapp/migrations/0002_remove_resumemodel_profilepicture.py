# Generated by Django 3.1 on 2020-10-10 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resumemodel',
            name='profilepicture',
        ),
    ]