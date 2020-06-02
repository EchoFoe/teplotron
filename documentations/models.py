from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class Document(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None, verbose_name='Наименование документа')
    slug = models.SlugField(max_length=200, blank=True, null=True, default=None, db_index=True, verbose_name='Слаг')
    position = models.IntegerField(default=None, blank=True, null=True,
                                   validators=[MinValueValidator(0), MaxValueValidator(30)], verbose_name='Позиция')
    available = models.BooleanField(default=True, verbose_name='Актуальность')
    mention = models.URLField(max_length=1024, blank=True, default=None, null=None, verbose_name='Ссылка из репозитория')
    file = models.FileField(upload_to='documents/%Y/%m/%d', blank=True, null=True, default=None, verbose_name='Файл')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования записи')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        ordering = ['position']
        verbose_name = 'Официальные документы'
        verbose_name_plural = 'Официальные документы'
