# Generated by Django 5.0.1 on 2024-04-08 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_admin_award'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='show_images/'),
        ),
    ]