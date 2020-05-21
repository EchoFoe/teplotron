from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils import timezone
from django.urls import reverse


class Comment(models.Model):
    first_name = models.CharField(max_length=32, blank=True, null=True, default=True, verbose_name='Имя')
    last_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='Фамилия')
    message = models.TextField(max_length=2056, null=True, blank=True, default=None, verbose_name='Отзыв')
    image = models.ImageField(upload_to='reviews/%Y/%m/%d', blank=True,
                              verbose_name='Фото')
    available = models.BooleanField(default=True, verbose_name='Актуальность отзыва')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания отзыва')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования отзыва')

    @property
    def Отзыв(self):
        return truncatechars(self.message, 150)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        ordering = ['-created']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
