# Generated by Django 2.2.12 on 2020-05-13 10:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0038_auto_20200512_2323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.AlterField(
            model_name='mail',
            name='resp',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]