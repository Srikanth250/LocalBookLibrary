# Generated by Django 3.0.6 on 2020-05-21 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0002_auto_20200521_1959'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='book',
            unique_together=set(),
        ),
    ]