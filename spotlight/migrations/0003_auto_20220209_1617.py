# Generated by Django 3.2.12 on 2022-02-09 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotlight', '0002_auto_20220208_2102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='videofile',
            new_name='videoFile',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='ethenicity',
            new_name='ethnicity',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='coutnry',
            new_name='country',
        ),
    ]