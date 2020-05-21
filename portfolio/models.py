from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


class Portfolio(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название выполненного объекта')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Слаг')
    image = models.ImageField(upload_to='portfolio_avatar/%Y/%m/%d', blank=True, verbose_name='Аватар объекта')
    # tittle = models.TextField(max_length=512, blank=True, verbose_name='Заголовок')
    # position = models.IntegerField(default=None, blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(20)], verbose_name='Позиция')
    description = models.TextField(max_length=2056, blank=True, verbose_name='Описание работ')
    available = models.BooleanField(default=False, verbose_name='Актуальность')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    class Meta:
        ordering = ('created', 'name')
        index_together = (('id', 'slug'),)
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('portfolio:portfolio_detail', args=[self.id, self.slug])


class PortfolioDetails(models.Model):
    portfolio = models.ForeignKey(Portfolio, blank=True, null=True, default=None, on_delete=models.CASCADE,
                                  verbose_name='Объект')
    image = models.ImageField(upload_to='portfolios/%Y/%m/%d', blank=True, verbose_name='Доп. фото')
    available = models.BooleanField(default=True, blank=True, null=True, verbose_name='Активный?')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return '%s' % self.portfolio

    class Meta:
        verbose_name = 'Подробная информация к объекту'
        verbose_name_plural = 'Подробная информация к объекту'
