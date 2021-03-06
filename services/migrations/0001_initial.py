# Generated by Django 3.0.6 on 2020-05-20 13:24

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Наименование услуги')),
                ('slug', models.SlugField(max_length=200, verbose_name='Слаг')),
                ('tittle', models.TextField(blank=True, max_length=1024, verbose_name='Заголовок')),
                ('image', models.ImageField(blank=True, upload_to='services/%Y/%m/%d', verbose_name='Фото')),
                ('position', models.IntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Позиция')),
                ('description', models.TextField(blank=True, max_length=2056, verbose_name='Описание работ')),
                ('available', models.BooleanField(default=False, verbose_name='Актуальность')),
                ('created', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата создания записи')),
                ('updated', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата ред-ия записи')),
            ],
            options={
                'verbose_name': 'Услуги',
                'verbose_name_plural': 'Услуги',
                'ordering': ('position', 'name'),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
