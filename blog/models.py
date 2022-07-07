from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=20, default='User')
    image = models.ImageField(upload_to='static/posts')
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'Author: {self.author}, Title:{self.title}'
