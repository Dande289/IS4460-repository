# Generated by Django 5.0.1 on 2024-04-09 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_character_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='show_images/'),
        ),
    ]
