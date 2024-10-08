# Generated by Django 5.0.7 on 2024-08-11 15:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teachingstaff',
            options={'ordering': ['order', 'role', 'name']},
        ),
        migrations.RemoveField(
            model_name='teachingstaff',
            name='subjects',
        ),
        migrations.AddField(
            model_name='teachingstaff',
            name='role',
            field=models.CharField(choices=[('principal', 'Principal'), ('deputy_admin', 'Deputy Admin'), ('deputy_academic', 'Deputy Academic'), ('teacher', 'Teacher')], default='teacher', max_length=20),
        ),
        migrations.AddField(
            model_name='teachingstaff',
            name='subject1',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachingstaff',
            name='subject2',
            field=models.CharField(default='sib', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teachingstaff',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='teachingstaff',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
