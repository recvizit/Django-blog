# Generated by Django 4.0.5 on 2022-07-01 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='desc',
        ),
    ]
