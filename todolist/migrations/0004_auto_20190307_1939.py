# Generated by Django 2.1.2 on 2019-03-07 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_todo_work_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='work_time',
            field=models.IntegerField(default=0),
        ),
    ]
