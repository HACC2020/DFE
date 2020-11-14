# Generated by Django 3.0.5 on 2020-11-10 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0005_applications_subowneragencyname'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applications',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='projects',
            name='subOwnerAgencyName',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]