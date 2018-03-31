# Generated by Django 2.0.3 on 2018-03-31 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_task_assign'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['project', 'task_name']},
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='slug-field', verbose_name='shortcut'),
            preserve_default=False,
        ),
    ]
