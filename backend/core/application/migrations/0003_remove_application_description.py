# Generated by Django 5.0.2 on 2024-03-30 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_application', '0002_userapplicationauthorization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='description',
        ),
    ]
