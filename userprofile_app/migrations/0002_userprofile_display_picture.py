# Generated by Django 4.2.7 on 2023-11-24 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='display_picture',
            field=models.URLField(default={}),
            preserve_default=False,
        ),
    ]
