# Generated by Django 2.2.12 on 2020-05-11 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_auto_20200511_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_img',
        ),
    ]
