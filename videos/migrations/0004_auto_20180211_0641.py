# Generated by Django 2.0.1 on 2018-02-11 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_auto_20180115_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='videos'),
        ),
    ]
