# Generated by Django 2.2.4 on 2019-08-04 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20190804_1340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='user',
            new_name='username',
        ),
    ]