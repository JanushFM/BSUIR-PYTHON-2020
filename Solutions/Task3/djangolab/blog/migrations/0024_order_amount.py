# Generated by Django 2.2.12 on 2020-05-10 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20200510_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(null=True),
        ),
    ]