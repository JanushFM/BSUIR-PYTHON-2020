# Generated by Django 2.2.12 on 2020-05-13 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0039_auto_20200513_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='resp',
            field=models.ManyToManyField(to='blog.Customer'),
        ),
    ]
