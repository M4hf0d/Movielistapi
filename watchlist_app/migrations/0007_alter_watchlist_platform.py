# Generated by Django 3.2.13 on 2022-05-15 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0006_alter_watchlist_platform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='platform',
            field=models.ManyToManyField(to='watchlist_app.StreamPlatform'),
        ),
    ]
