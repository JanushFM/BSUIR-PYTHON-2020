# Generated by Django 2.2.12 on 2020-05-10 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20200510_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='price',
            field=models.FloatField(max_length=40, null=True),
        ),
    ]
