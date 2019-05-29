# Generated by Django 2.1.7 on 2019-03-26 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20190326_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permissioncompany',
            name='permission_users',
        ),
        migrations.AddField(
            model_name='permissioncompany',
            name='permission_companies',
            field=models.ManyToManyField(blank=True, help_text='access to company data', related_name='companies', to='todo.Company'),
        ),
    ]