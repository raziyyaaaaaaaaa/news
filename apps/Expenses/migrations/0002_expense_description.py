# Generated by Django 5.0.3 on 2024-03-05 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expenses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
