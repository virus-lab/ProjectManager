# Generated by Django 2.1.5 on 2019-01-21 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': '프로젝트', 'verbose_name_plural': '프로젝트'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': '작업', 'verbose_name_plural': '작업'},
        ),
        migrations.RemoveField(
            model_name='task',
            name='archived',
        ),
        migrations.AddField(
            model_name='task',
            name='archive',
            field=models.BooleanField(default=False, verbose_name='아카이브 여부'),
        ),
    ]
