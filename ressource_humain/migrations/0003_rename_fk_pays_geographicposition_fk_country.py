# Generated by Django 5.0.4 on 2024-05-06 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ressource_humain', '0002_presence_subvention_curriculumvitae_file_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='geographicposition',
            old_name='fk_pays',
            new_name='fk_country',
        ),
    ]
