# Generated by Django 3.1.7 on 2021-03-12 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210312_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default=0, max_length=15, unique=True),
        ),
    ]
