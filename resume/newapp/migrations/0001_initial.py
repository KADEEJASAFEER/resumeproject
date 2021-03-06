# Generated by Django 3.1 on 2020-10-10 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=20)),
                ('lastdegree', models.CharField(max_length=50)),
                ('profilepicture', models.ImageField(upload_to='images')),
            ],
        ),
    ]
