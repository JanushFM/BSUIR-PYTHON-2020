# Generated by Django 2.2.12 on 2020-05-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0041_auto_20200513_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyMail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_subject', models.CharField(max_length=100, verbose_name='Заголовок сообщения')),
                ('email_text', models.TextField(null=True, verbose_name='Текст сообщения')),
                ('email_date', models.DateField(null=True, verbose_name='Время отправки')),
                ('email_time', models.TimeField(null=True)),
                ('recipients', models.ManyToManyField(to='blog.Customer')),
            ],
        ),
        migrations.DeleteModel(
            name='Mail',
        ),
    ]