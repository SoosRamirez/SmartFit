# Generated by Django 4.1 on 2022-09-13 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_blogpost_options_alter_blogpost_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
