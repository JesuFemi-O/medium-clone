# Generated by Django 2.0.6 on 2018-09-20 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.TextField(blank=True),
        ),
    ]
