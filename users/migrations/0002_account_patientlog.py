# Generated by Django 3.0.3 on 2021-05-03 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(max_length=3, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Account')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Patient')),
            ],
        ),
    ]
