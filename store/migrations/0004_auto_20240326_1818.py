# Generated by Django 3.1 on 2024-03-26 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_reviewrating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewrating',
            old_name='subjects',
            new_name='subject',
        ),
    ]