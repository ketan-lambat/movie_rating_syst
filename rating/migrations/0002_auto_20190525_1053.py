# Generated by Django 2.2.1 on 2019-05-25 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(verbose_name='date released'),
        ),
    ]