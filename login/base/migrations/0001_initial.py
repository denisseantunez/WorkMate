# Generated by Django 4.2.16 on 2024-10-23 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=50)),
                ('icon', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]