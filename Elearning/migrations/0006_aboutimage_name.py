# Generated by Django 4.2 on 2023-04-30 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elearning', '0005_aboutimage_remove_about_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutimage',
            name='name',
            field=models.CharField(default='new', max_length=10),
            preserve_default=False,
        ),
    ]