# Generated by Django 3.2.12 on 2022-02-10 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spotlight', '0006_alter_movie_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='Role',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='actor',
            old_name='User',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='Actor',
            new_name='actor',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='Movie',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='Role',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='User',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='vote',
            old_name='Actor',
            new_name='actor',
        ),
        migrations.RenameField(
            model_name='vote',
            old_name='User',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='movie',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='spotlight.user'),
        ),
    ]
