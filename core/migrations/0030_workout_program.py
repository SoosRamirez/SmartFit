# Generated by Django 4.1 on 2022-09-20 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_workoutprogram'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='program',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.workoutprogram'),
        ),
    ]