# Generated by Django 2.0.1 on 2018-01-15 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='rating',
            field=models.CharField(choices=[('G', 'General'), ('PG', 'Parental Guidance'), ('PG-13', 'Parents Strongly Cautioned'), ('R', 'Restricted'), ('NC-17', 'Adults Only')], default='PG-13', max_length=16),
        ),
    ]
