from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


class New(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Заголовок новости')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Слаг')
    image = models.ImageField(upload_to='news/%Y/%m/%d', blank=True, verbose_name='Фото')
    tittle = models.TextField(max_length=512, verbose_name='Краткое описание к новости')
    description = models.TextField(max_length=10000, blank=True, verbose_name='Текст новости')
    available = models.BooleanField(default=False, verbose_name='Актуальность')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    class Meta:
        ordering = ['-created']
        index_together = (('id', 'slug'),)
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('news:news_detail', args=[self.id, self.slug])
