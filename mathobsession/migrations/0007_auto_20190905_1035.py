# Generated by Django 2.2.5 on 2019-09-05 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mathobsession', '0006_exercise_sketches'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='sketches',
            new_name='sketch',
        ),
    ]
