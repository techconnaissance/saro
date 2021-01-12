# Generated by Django 3.1.4 on 2021-01-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField()),
                ('message', models.CharField(max_length=2083)),
                ('is_addressed', models.BooleanField()),
                ('added_date', models.DateTimeField()),
                ('added_by', models.CharField(max_length=50)),
                ('updated_date', models.DateTimeField()),
                ('updated_by', models.CharField(max_length=50)),
            ],
        ),
    ]
