# Generated by Django 3.2.3 on 2021-09-24 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('picture', models.ImageField(upload_to='')),
                ('address', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=6)),
                ('link', models.URLField(max_length=100)),
                ('schedule', models.DateTimeField()),
            ],
        ),
    ]
