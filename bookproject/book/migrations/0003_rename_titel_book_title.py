# Generated by Django 5.1.2 on 2025-06-24 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_delete_samplmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='titel',
            new_name='title',
        ),
    ]
