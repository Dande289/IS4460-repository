# Generated by Django 5.0.1 on 2024-03-20 22:45

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_items', models.IntegerField()),
                ('order_date', models.DateField(default=datetime.datetime(2024, 3, 20, 22, 45, 53, 451250, tzinfo=datetime.timezone.utc))),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]