# Generated by Django 4.0.5 on 2022-09-12 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostForHer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='User', max_length=20)),
                ('image', models.ImageField(upload_to='static/posts')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('ingredients', models.TextField(max_length=500)),
                ('description', models.TextField(max_length=1500)),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.CreateModel(
            name='PostForHim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='User', max_length=20)),
                ('image', models.ImageField(upload_to='static/posts')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('ingredients', models.TextField(max_length=500)),
                ('description', models.TextField(max_length=1500)),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
