# Generated by Django 4.0 on 2021-12-26 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zobin_web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='dla_mnie',
            field=models.BooleanField(null=True),
        ),
    ]
