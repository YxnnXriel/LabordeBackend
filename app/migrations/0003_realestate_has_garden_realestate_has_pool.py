# Generated by Django 5.1.4 on 2024-12-09 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_realestate_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='realestate',
            name='has_garden',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='realestate',
            name='has_pool',
            field=models.BooleanField(default=False),
        ),
    ]
