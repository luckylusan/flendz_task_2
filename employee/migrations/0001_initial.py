# Generated by Django 3.1.7 on 2021-04-17 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=200)),
                ('emp_designation', models.CharField(max_length=200)),
                ('emp_doj', models.DateField()),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]
