# Generated by Django 3.2.18 on 2023-04-10 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smallblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]