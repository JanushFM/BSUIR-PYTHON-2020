# Generated by Django 2.2.12 on 2020-05-11 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]