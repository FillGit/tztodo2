# Generated by Django 2.1.7 on 2019-03-24 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='RGD, Aeroflot, Rosneft, Gazprom or empty', max_length=50)),
                ('permission_users', models.ManyToManyField(blank=True, help_text='access to company data', related_name='companies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Desk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('done', models.BooleanField(default=False)),
                ('due_date', models.DateField()),
                ('task', models.TextField()),
                ('executor', models.CharField(blank=True, help_text='User executor', max_length=50, null=True)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Company')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='desks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_idsession', models.DateField(blank=True, null=True)),
                ('idsession', models.CharField(blank=True, max_length=50)),
                ('active_for_company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='todo.Company')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
