# Generated by Django 4.0.5 on 2022-06-08 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0007_alter_auto_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='photo',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]
