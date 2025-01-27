# Generated by Django 5.1.1 on 2024-11-22 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0003_alter_customuser_managers_customuser_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missingperson',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], default='Female', max_length=10),
        ),
        migrations.AlterField(
            model_name='missingperson',
            name='lastSeenDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='missingperson',
            name='lastSeenLocation',
            field=models.CharField(max_length=120),
        ),
    ]
