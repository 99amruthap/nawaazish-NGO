# Generated by Django 3.0.6 on 2020-07-06 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JoinUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=300)),
                ('area', models.CharField(max_length=100)),
                ('pincode', models.PositiveIntegerField()),
                ('phone', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('insta', models.CharField(max_length=30)),
                ('feedback', models.TextField()),
            ],
        ),
    ]
