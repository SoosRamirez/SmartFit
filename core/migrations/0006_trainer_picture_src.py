# Generated by Django 4.1 on 2022-09-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_trainer_programs'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='picture_src',
            field=models.CharField(default='', max_length=50, verbose_name='Адрес картинки'),
        ),
    ]