# Generated by Django 2.2.12 on 2020-05-17 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0053_auto_20200517_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='price',
            field=models.FloatField(max_length=40, null=True),
        ),
    ]