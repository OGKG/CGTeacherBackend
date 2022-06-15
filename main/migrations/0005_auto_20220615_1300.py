# Generated by Django 3.2 on 2022-06-15 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_task_pickle_dump'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='pickle_dump',
        ),
        migrations.AddField(
            model_name='task',
            name='answers',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='task',
            name='condition',
            field=models.JSONField(default=dict),
        ),
    ]
