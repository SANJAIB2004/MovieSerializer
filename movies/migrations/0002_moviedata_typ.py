# Generated by Django 5.1.5 on 2025-01-30 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='typ',
            field=models.CharField(default='action', max_length=100),
        ),
    ]
