from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


class AboutUs(models.Model):
    name = models.CharField(blank=True, null=True, default=None, max_length=200, verbose_name='Название компании')
    tittle = models.TextField(max_length=512, blank=True, verbose_name='Заголовок "О компании"')
    image = models.ImageField(upload_to='about_us/%Y/%m/%d', blank=True, verbose_name='Фото')
    description = models.TextField(max_length=2056, blank=True, verbose_name='Описание компании')
    address = models.CharField(max_length=1024, blank=True, null=True, verbose_name='Адрес')
    email = models.EmailField(max_length=128, blank=True, null=True, default=None, verbose_name='Емейл')
    phone = models.CharField(max_length=128, blank=True, null=True, default=None, verbose_name='Номер тел.')
    schedule_start = models.TimeField(blank=True, null=True, verbose_name='Н. раб. дня (Пн - Пт)')
    schedule_end = models.TimeField(blank=True, null=True, verbose_name='К. раб. дня (Пн - Пт)')
    available = models.BooleanField(default=True, verbose_name='Актуальность')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    class Meta:
        ordering = ['created']
        verbose_name = 'О компании'
        verbose_name_plural = 'О компании'

    def __str__(self):
        return '%s' % self.name


class AboutUsDetails(models.Model):
    name = models.ForeignKey(AboutUs, blank=True, null=True, default=None, on_delete=models.CASCADE,
                             verbose_name='Компания')
    is_main = models.BooleanField(default=False, blank=True, null=True, verbose_name='Главный филиал?')
    is_not_main = models.BooleanField(default=True, blank=True, null=True, verbose_name='Доп. офис')
    available = models.BooleanField(default=True, blank=True, null=True, verbose_name='Активный?')
    address = models.CharField(max_length=1024, blank=True, null=True, verbose_name='Адрес')
    email = models.EmailField(max_length=128, blank=True, null=True, default=None, verbose_name='Емейл')
    phone = models.CharField(max_length=128, blank=True, null=True, default=None, verbose_name='Номер тел.')
    schedule_start = models.TimeField(blank=True, null=True, verbose_name='Н. раб. дня (Пн - Пт)')
    schedule_end = models.TimeField(blank=True, null=True, verbose_name='К. раб. дня (Пн - Пт)')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Подробная информация к компании'
        verbose_name_plural = 'Подробная информация к компании'


class Partners(models.Model):
    name = models.CharField(blank=True, null=True, default=None, max_length=200, verbose_name='Название партнера')
    image = models.ImageField(upload_to='partners/%Y/%m/%d', blank=True, verbose_name='Логотип (высота логотипа не должна превышать 40 px!')
    available = models.BooleanField(default=True, verbose_name='Актуальность')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    class Meta:
        ordering = ['created']
        verbose_name = 'Партнеры'
        verbose_name_plural = 'Партнеры'

    def __str__(self):
        return '%s' % self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Имя')
    last_name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Фамилия')
    email = models.EmailField(max_length=128, blank=True, null=True, default=None, verbose_name='Емейл')
    phone = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Номер тел.')
    message = models.TextField(max_length=512, blank=True, verbose_name='Текст обращения')
    status = models.BooleanField(default=False, verbose_name='Вопрос решен?')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата заявления')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return 'Клиент: %s %s, почта: %s' % (self.first_name, self.last_name, self.email)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)
