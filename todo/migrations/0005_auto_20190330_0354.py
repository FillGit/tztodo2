# Generated by Django 2.1.7 on 2019-03-30 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20190329_0453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='active_for_company',
        ),
        migrations.RemoveField(
            model_name='session',
            name='username',
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
        migrations.DeleteModel(
            name='Session',
        ),
    ]
