# Generated by Django 5.1.4 on 2025-01-10 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivarity',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
