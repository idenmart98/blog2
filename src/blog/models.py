from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    body = models.TextField(max_length=1500, verbose_name=' Тело Поста')
    tags = models.ManyToManyField(Tag, related_name='posts', verbose_name='Теги')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
