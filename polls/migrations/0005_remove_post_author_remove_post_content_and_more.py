# Generated by Django 4.2.10 on 2024-03-03 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_author_unique_name_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]