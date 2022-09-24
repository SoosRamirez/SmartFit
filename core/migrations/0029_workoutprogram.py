# Generated by Django 4.1 on 2022-09-20 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_alter_trainer_direction'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.TimeField(auto_created=True, default='00:00:00')),
                ('name', models.CharField(max_length=30)),
                ('picture_src', models.CharField(default='', max_length=50, verbose_name='Адрес картинки')),
                ('calories', models.IntegerField(default=0)),
                ('amount_of_workouts', models.IntegerField(default=0)),
                ('description', models.TextField(max_length=200)),
                ('level', models.CharField(choices=[('1', 'Новичек'), ('2', 'Любитель'), ('3', 'Продвинутый'), ('4', 'Профессионал')], max_length=1)),
                ('directions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.direction')),
                ('trainer', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='core.trainer')),
            ],
            options={
                'verbose_name': 'Программа',
            },
        ),
    ]
