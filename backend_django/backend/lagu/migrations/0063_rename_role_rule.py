# Generated by Django 4.2.5 on 2023-11-16 02:31

from django.db import migrations



class Migration(migrations.Migration):

    dependencies = [
        ('lagu', '0062_alter_role_unit'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Role',
            new_name='Rule',
        ),
    ]