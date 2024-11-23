# Generated by Django 5.1.3 on 2024-11-09 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Missingperson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=10)),
                ('lastSeenDate', models.DateTimeField()),
                ('lastSeenLocation', models.DateTimeField()),
                ('description', models.TextField()),
                ('uploadPhoto', models.ImageField(upload_to='')),
                ('contactInformation', models.CharField(max_length=12)),
                ('status', models.CharField(choices=[('missing', 'Missing'), ('found', 'Found')], default='missing', max_length=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'missingperson',
            },
        ),
    ]
