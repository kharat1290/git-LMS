# Generated by Django 4.1.1 on 2022-10-26 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('auther_name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('type_of_book', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'BookModel',
            },
        ),
    ]
