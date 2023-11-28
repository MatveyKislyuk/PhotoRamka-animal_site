# Generated by Django 4.2.7 on 2023-11-28 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Изображение'),
        ),
        migrations.RemoveField(
            model_name='image',
            name='tags',
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='image',
            name='tags',
            field=models.CharField(default='', max_length=255, verbose_name='Теги'),
            preserve_default=False,
        ),
    ]
