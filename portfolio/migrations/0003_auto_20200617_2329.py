# Generated by Django 3.0.7 on 2020-06-18 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200617_2308'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Repository',
            new_name='RepositoryMetadata',
        ),
    ]