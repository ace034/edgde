# Generated by Django 2.0.1 on 2018-01-15 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180115_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='color',
            field=models.CharField(choices=[('yellow', 'Yellow'), ('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('pink', 'Pink'), ('gray', 'Gray'), ('black', 'Black'), ('orange', 'Orange')], default='red', max_length=16),
        ),
    ]
