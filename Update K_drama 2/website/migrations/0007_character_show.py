# Generated by Django 5.0.1 on 2024-04-09 01:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_character_delete_admin_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='show',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actor', to='website.show'),
        ),
    ]
