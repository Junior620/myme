# Generated by Django 4.0 on 2023-07-02 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0025_inscriptionformulaire_date_naissance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscriptionformulaire',
            name='telephone',
        ),
    ]
