# Generated by Django 2.2.12 on 2020-05-09 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_painting_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='author',
            field=models.CharField(max_length=144, null=True),
        ),
    ]
