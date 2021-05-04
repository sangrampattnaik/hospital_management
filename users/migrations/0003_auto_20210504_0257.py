# Generated by Django 3.0.3 on 2021-05-04 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_account_patientlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventcategory',
            name='category',
            field=models.CharField(choices=[('1', 'Procedure'), ('2', 'Prescription'), ('3', 'Test')], default='1', max_length=5),
        ),
    ]