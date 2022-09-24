# Generated by Django 4.1 on 2022-09-13 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_trainer_workouts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=20)),
                ('video', models.CharField(max_length=100)),
                ('trainer', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='core.trainer')),
            ],
            options={
                'verbose_name': 'Тренировка',
            },
        ),
    ]
