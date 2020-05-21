from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class Expert(models.Model):
    first_name = models.CharField(max_length=128, blank=True, null=True, default=None, verbose_name='Имя')
    last_name = models.CharField(max_length=128, blank=True, null=True, default=None, verbose_name='Фамилия')
    office = models.CharField(max_length=256, blank=True, null=True, default=None, verbose_name='Должность')
    position = models.IntegerField(default=None, blank=True, null=True,
                                   validators=[MinValueValidator(0), MaxValueValidator(20)], verbose_name='Позиция')
    email = models.EmailField(max_length=128, blank=True, null=True, default=None, verbose_name='Емейл')
    phone = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Номер тел.')
    dob = models.DateField(default=None, null=True, blank=True, verbose_name='Дата рожд-я')
    country = models.CharField(max_length=64, null=True, blank=True, default='Россия', verbose_name='Страна')
    town = models.CharField(max_length=64, blank=True, default='Курск', verbose_name='Город')
    image = models.ImageField(upload_to='experts/%Y/%m/%d', blank=True, verbose_name='Фото')
    description = models.TextField(max_length=512, null=True, blank=True, default=None,
                                   verbose_name='Описание деятельности')
    available = models.BooleanField(default=True, verbose_name='Актуальность')
    vk = models.URLField(max_length=1024, blank=True, default=None, null=None, verbose_name='Ссылка VK')
    instagram = models.URLField(max_length=1024, blank=True, default=None, null=None, verbose_name='Ссылка instagram')
    twitter = models.URLField(max_length=1024, blank=True, default=None, null=None, verbose_name='Ссылка twitter')
    facebook = models.URLField(max_length=1024, blank=True, default=None, null=None, verbose_name='Ссылка facebook')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования записи')

    def __str__(self):
        return "%s" % self.last_name

    class Meta:
        ordering = ['position']
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'
