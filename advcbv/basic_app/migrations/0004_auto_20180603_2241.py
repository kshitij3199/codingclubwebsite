# Generated by Django 2.0.2 on 2018-06-03 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_auto_20180603_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='project_current',
        ),
        migrations.RemoveField(
            model_name='student',
            name='project_done',
        ),
        migrations.AddField(
            model_name='student',
            name='skills',
            field=models.CharField(default='N.A.', max_length=256),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(default='N.A.', max_length=254),
        ),
        migrations.AlterField(
            model_name='student',
            name='github',
            field=models.CharField(default='N.A.', max_length=256),
        ),
        migrations.AlterField(
            model_name='student',
            name='interest',
            field=models.CharField(default='N.A.', max_length=256),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.CharField(default='N.A.', max_length=256),
        ),
    ]