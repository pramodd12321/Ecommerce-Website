# Generated by Django 3.1 on 2020-09-07 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_auto_20200907_1414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='emaile',
            new_name='email',
        ),
    ]
