# Generated by Django 3.1.7 on 2021-06-08 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathesar', '0004_auto_20210604_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schema',
            name='name',
        ),
        migrations.RemoveField(
            model_name='table',
            name='name',
        ),
        migrations.AddField(
            model_name='schema',
            name='oid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='table',
            name='oid',
            field=models.IntegerField(default=10000),
            preserve_default=False,
        ),
    ]