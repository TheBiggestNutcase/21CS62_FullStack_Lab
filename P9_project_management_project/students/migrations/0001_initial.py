# Generated by Django 4.2.11 on 2024-05-04 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=200)),
                ('languages_used', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
            ],
        ),
    ]
