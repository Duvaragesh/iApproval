# Generated by Django 2.1.2 on 2018-12-11 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empid', models.CharField(max_length=30)),
                ('Firstname', models.CharField(max_length=30)),
                ('Lastname', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=60)),
                ('Team_Name', models.CharField(max_length=50)),
                ('Request_Number', models.CharField(max_length=50)),
                ('Request_Status', models.CharField(max_length=50)),
                ('Sub_Request_Number', models.CharField(max_length=50)),
                ('Sub_Request_Status', models.CharField(max_length=50)),
            ],
        ),
    ]
