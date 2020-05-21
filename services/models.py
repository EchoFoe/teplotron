from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


class Service(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование услуги')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Слаг')
    tittle = models.TextField(max_length=1024, blank=True, verbose_name='Заголовок')
    image = models.ImageField(upload_to='services/%Y/%m/%d', blank=True, verbose_name='Фото')
    position = models.IntegerField(default=None, blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(20)], verbose_name='Позиция')
    description = models.TextField(max_length=2056, blank=True, verbose_name='Описание работ')
    available = models.BooleanField(default=False, verbose_name='Актуальность')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    class Meta:
        ordering = ('position', 'name')
        index_together = (('id', 'slug'),)
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('home:service_detail', args=[self.id, self.slug])
