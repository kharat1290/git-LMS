# Generated by Django 4.1.1 on 2022-10-26 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmodel',
            old_name='auther_name',
            new_name='author_name',
        ),
    ]
