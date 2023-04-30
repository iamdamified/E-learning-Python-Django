# Generated by Django 4.2 on 2023-04-30 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elearning', '0002_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('introduction', models.CharField(max_length=100)),
                ('description1', models.TextField()),
                ('description2', models.TextField()),
                ('image', models.ImageField(upload_to='about_image')),
            ],
        ),
    ]
