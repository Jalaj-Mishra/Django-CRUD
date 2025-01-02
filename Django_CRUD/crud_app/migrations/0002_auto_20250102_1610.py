# Generated by Django 3.1.12 on 2025-01-02 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetail',
            fields=[
                ('empId', models.IntegerField(max_length=3, primary_key=True, serialize=False)),
                ('empName', models.CharField(max_length=100)),
                ('empEmail', models.EmailField(max_length=100)),
                ('empPassword', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='EmployeeDetails',
        ),
    ]