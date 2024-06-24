# Generated by Django 5.0.6 on 2024-06-23 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='date',
            new_name='data',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='description',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='name',
            new_name='local',
        ),
        migrations.AddField(
            model_name='event',
            name='nome',
            field=models.CharField(default='Evento Padrão', max_length=100),
            preserve_default=False,
        ),
    ]