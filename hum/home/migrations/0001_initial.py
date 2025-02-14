# Generated by Django 4.0.3 on 2022-03-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('uname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=250)),
                ('passw', models.CharField(max_length=50)),
                ('states', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('phone_n', models.CharField(max_length=15)),
                ('dob', models.CharField(max_length=15)),
            ],
        ),
    ]
