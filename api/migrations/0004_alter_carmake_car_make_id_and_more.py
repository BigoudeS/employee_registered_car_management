# Generated by Django 5.0.4 on 2024-04-24 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_employee_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmake',
            name='car_make_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='car_model_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employeecar',
            name='employee_car_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
