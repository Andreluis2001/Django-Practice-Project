# Generated by Django 5.1.7 on 2025-03-13 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('serial_number', models.CharField(max_length=100)),
                ('processor_model', models.CharField(max_length=100)),
                ('installed_ram', models.PositiveIntegerField()),
                ('installd_storage', models.PositiveIntegerField()),
            ],
        ),
    ]
