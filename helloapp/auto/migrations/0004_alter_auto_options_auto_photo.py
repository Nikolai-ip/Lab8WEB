# Generated by Django 4.0.5 on 2022-06-08 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0003_remove_auto_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auto',
            options={'verbose_name': 'Автомобиль', 'verbose_name_plural': 'Автомобили'},
        ),
        migrations.AddField(
            model_name='auto',
            name='photo',
            field=models.ImageField(default=False, upload_to='photo/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]