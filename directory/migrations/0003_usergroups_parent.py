# Generated by Django 3.0.5 on 2020-11-06 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_percents'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroups',
            name='parent',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
