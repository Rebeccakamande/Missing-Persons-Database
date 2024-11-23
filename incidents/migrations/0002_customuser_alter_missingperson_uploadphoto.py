# Generated by Django 5.1.3 on 2024-11-09 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'customUser',
            },
        ),
        migrations.AlterField(
            model_name='missingperson',
            name='uploadPhoto',
            field=models.ImageField(upload_to='uploads/missingpeople/'),
        ),
    ]
