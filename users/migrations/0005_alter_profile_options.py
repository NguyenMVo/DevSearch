# Generated by Django 3.2.4 on 2021-11-15 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['created']},
        ),
    ]
