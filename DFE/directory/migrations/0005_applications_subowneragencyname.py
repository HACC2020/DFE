# Generated by Django 3.0.5 on 2020-11-09 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0004_auto_20201106_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='subOwnerAgencyName',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
