# Generated by Django 2.2.5 on 2019-09-04 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mathobsession', '0003_auto_20190904_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='subject',
            new_name='subjects',
        ),
    ]
