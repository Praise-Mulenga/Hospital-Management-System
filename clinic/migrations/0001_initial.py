# Generated by Django 4.2.5 on 2023-09-23 18:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ward',
            fields=[
                ('ward_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('ward_name', models.CharField(max_length=25)),
                ('number_beds', models.IntegerField()),
                ('nurse_in_charge', models.CharField(max_length=20)),
                ('ward_type', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('patient_id', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('initials', models.CharField(max_length=2)),
                ('sex', models.CharField(max_length=1)),
                ('address', models.CharField(max_length=30)),
                ('post_code', models.CharField(max_length=3)),
                ('admission', models.DateField()),
                ('DOB', models.DateField(default=django.utils.timezone.now)),
                ('next_of_kin', models.CharField(max_length=30, null=True)),
                ('ward_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.ward')),
            ],
        ),
    ]