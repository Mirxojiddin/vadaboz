# Generated by Django 4.2 on 2024-06-22 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_city_alter_customuser_district_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='name',
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_photo',
            field=models.ImageField(default='default_photo.jpg', upload_to=''),
        ),
    ]
