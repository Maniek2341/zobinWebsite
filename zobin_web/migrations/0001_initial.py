# Generated by Django 4.0 on 2021-12-26 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('tresc', models.TextField(max_length=255)),
            ],
        ),
    ]
