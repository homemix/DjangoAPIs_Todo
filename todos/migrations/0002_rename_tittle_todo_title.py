# Generated by Django 4.1.5 on 2023-01-13 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='tittle',
            new_name='title',
        ),
    ]
