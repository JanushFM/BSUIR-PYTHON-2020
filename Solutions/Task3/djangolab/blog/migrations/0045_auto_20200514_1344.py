# Generated by Django 2.2.12 on 2020-05-14 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0044_auto_20200513_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='description_big',
            field=models.TextField(max_length=4000, null='No BIG description provided'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='description_small',
            field=models.TextField(max_length=200, null='No SMALL description provided'),
        ),
    ]
