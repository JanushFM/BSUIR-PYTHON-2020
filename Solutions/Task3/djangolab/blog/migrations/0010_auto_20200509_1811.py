# Generated by Django 2.2.12 on 2020-05-09 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_painting_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='price',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
