# Generated by Django 4.0.4 on 2022-05-23 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0013_participants_collegename_participants_level1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participants',
            old_name='starttime',
            new_name='starttime1',
        ),
        migrations.AddField(
            model_name='participants',
            name='starttime2',
            field=models.CharField(default='0:0:0', max_length=10),
        ),
    ]
