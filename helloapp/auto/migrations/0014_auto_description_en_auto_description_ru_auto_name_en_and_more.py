# Generated by Django 4.0.5 on 2022-06-09 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0013_remove_auto_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
