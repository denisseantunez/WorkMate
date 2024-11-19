# Generated by Django 5.1.2 on 2024-11-14 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=300)),
                ('description', models.TextField(max_length=600)),
                ('category', models.CharField(choices=[('TEAM', 'WorkMate Internal'), ('DEV', 'Desarrollo'), ('TECH', 'Tecnologico'), ('OTHER', 'Otro/No Listado'), ('ADMIN', 'Administrativo')], max_length=20)),
                ('priority', models.IntegerField(choices=[(1, 'Level 1'), (2, 'Level 2'), (3, 'Level 3'), (4, 'Level 4'), (5, 'Level 5')], default=1)),
                ('notes', models.TextField(blank=True, max_length=300)),
                ('progress', models.IntegerField(choices=[(1, 'Completed'), (2, 'Incomplete'), (3, 'Not started')], default=3)),
            ],
        ),
    ]
