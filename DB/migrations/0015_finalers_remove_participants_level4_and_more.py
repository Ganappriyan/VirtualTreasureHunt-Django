# Generated by Django 4.0.4 on 2022-05-23 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0014_rename_starttime_participants_starttime1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finalers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname', models.CharField(default='NULL', max_length=50)),
                ('collegename', models.CharField(default='NULL', max_length=50)),
                ('starttime2', models.CharField(default='0:0:0', max_length=10)),
                ('level4', models.CharField(default='0:0:0', max_length=10)),
                ('level5', models.CharField(default='0:0:0', max_length=10)),
                ('totaltime2', models.CharField(default='0:0:0', max_length=10)),
                ('points2', models.IntegerField(default=-1)),
            ],
        ),
        migrations.RemoveField(
            model_name='participants',
            name='level4',
        ),
        migrations.RemoveField(
            model_name='participants',
            name='level5',
        ),
        migrations.RemoveField(
            model_name='participants',
            name='points2',
        ),
        migrations.RemoveField(
            model_name='participants',
            name='starttime2',
        ),
        migrations.RemoveField(
            model_name='participants',
            name='totaltime2',
        ),
    ]
