# Generated by Django 2.2.12 on 2020-05-17 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0054_auto_20200517_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='price',
            field=models.DecimalField(decimal_places=10, max_digits=19, null=True),
        ),
    ]
