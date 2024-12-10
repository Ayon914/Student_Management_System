# Generated by Django 5.1.3 on 2024-12-05 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_number', models.PositiveIntegerField()),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=100)),
                ('Field_of_study', models.CharField(max_length=50)),
                ('GPA', models.FloatField()),
            ],
        ),
    ]
