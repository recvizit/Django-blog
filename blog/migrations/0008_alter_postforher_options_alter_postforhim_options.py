# Generated by Django 4.0.5 on 2022-09-12 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_postforher_postforhim_delete_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postforher',
            options={'verbose_name': 'Пост для неё', 'verbose_name_plural': 'Посты для неё'},
        ),
        migrations.AlterModelOptions(
            name='postforhim',
            options={'verbose_name': 'Пост для него', 'verbose_name_plural': 'Посты для него'},
        ),
    ]
