# Generated by Django 4.0.4 on 2022-05-23 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0012_remove_participants_collegename_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='participants',
            name='collegename',
            field=models.CharField(default='NULL', max_length=50),
        ),
        migrations.AddField(
            model_name='participants',
            name='level1',
            field=models.CharField(default='0:0:0', max_length=10),
        ),
        migrations.AddField(
            model_name='participants',
            name='level2',
            field=models.CharField(default='0:0:0', max_length=10),
        ),
        migrations.AddField(
            model_name='participants',
            name='level3',
            field=models.CharField(default='0:0:0', max_length=10),
        ),
        migrations.AddField(
            model_name='participants',
            name='level4',
            field=models.CharField(default='0:0:0', max_length=10),
        ),
        migrations.AddField(
            model_name='participants',
            name='level5',
            field=models.CharField(default='0:0:0', max_length=10),
        ),
        migrations.AddField(
            model_name='participants',
            name='points1',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='participants',
            name='points2',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='participants',
            name='starttime',
            field=models.CharField(default='0:0:0', max_length=10),
        ),
        migrations.AddField(
            model_name='participants',
            name='teamname',
            field=models.CharField(default='NULL', max_length=50),
        ),
        migrations.AddField(
            model_name='participants',
            name='totaltime1',
            field=models.CharField(default='0:0:0', max_length=10),
        ),
        migrations.AddField(
            model_name='participants',
            name='totaltime2',
            field=models.CharField(default='0:0:0', max_length=10),
        ),
    ]
