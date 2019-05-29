# Generated by Django 2.1.7 on 2019-03-31 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20190331_0512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allowance',
            name='allowance_companies',
        ),
        migrations.RemoveField(
            model_name='allowance',
            name='username',
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'permissions': (('can_work_this_obj', 'Work this obj. Set permission Admin'), ('can_work_this_obj_sometime', 'Work this obj. Set permission User'))},
        ),
        migrations.DeleteModel(
            name='Allowance',
        ),
    ]
