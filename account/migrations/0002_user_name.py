# Generated by Django 3.0.5 on 2020-06-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=models.EmailField(max_length=254, unique=True), max_length=10, unique=True),
        ),
    ]