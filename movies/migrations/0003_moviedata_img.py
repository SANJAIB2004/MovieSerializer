# Generated by Django 5.1.5 on 2025-01-30 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviedata_typ'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='img',
            field=models.ImageField(default='Images/None/Noimg.jpg', upload_to='Images/'),
        ),
    ]
