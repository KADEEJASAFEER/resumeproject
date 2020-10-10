# Generated by Django 3.1 on 2020-10-10 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_resumemodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resumemodel',
            name='image',
        ),
        migrations.AlterField(
            model_name='resumemodel',
            name='dob',
            field=models.DateField(max_length=20),
        ),
        migrations.AlterField(
            model_name='resumemodel',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
