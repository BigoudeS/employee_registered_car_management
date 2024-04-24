# Generated by Django 5.0.4 on 2024-04-24 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmake',
            name='id',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='id',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.RemoveField(
            model_name='employeecar',
            name='id',
        ),
        migrations.AddField(
            model_name='carmake',
            name='car_make_id',
            field=models.AutoField(default='1', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='car_model_id',
            field=models.AutoField(default='1', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_id',
            field=models.AutoField(default='1', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='employeecar',
            name='employee_car_id',
            field=models.AutoField(default='1', primary_key=True, serialize=False),
        ),
    ]
