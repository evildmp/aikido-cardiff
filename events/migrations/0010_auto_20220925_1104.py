# Generated by Django 2.2.28 on 2022-09-25 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_forthcomingevents_style'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['start_date']},
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='ends'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(verbose_name='starts'),
        ),
    ]
