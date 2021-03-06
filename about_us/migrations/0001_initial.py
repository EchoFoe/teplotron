# Generated by Django 3.0.6 on 2020-05-20 13:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Название компании')),
                ('tittle', models.TextField(blank=True, max_length=512, verbose_name='Заголовок "О компании"')),
                ('image', models.ImageField(blank=True, upload_to='about_us/%Y/%m/%d', verbose_name='Фото')),
                ('description', models.TextField(blank=True, max_length=2056, verbose_name='Описание компании')),
                ('address', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Адрес')),
                ('email', models.EmailField(blank=True, default=None, max_length=128, null=True, verbose_name='Емейл')),
                ('phone', models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='Номер тел.')),
                ('schedule_start', models.TimeField(blank=True, null=True, verbose_name='Н. раб. дня (Пн - Пт)')),
                ('schedule_end', models.TimeField(blank=True, null=True, verbose_name='К. раб. дня (Пн - Пт)')),
                ('available', models.BooleanField(default=True, verbose_name='Актуальность')),
                ('created', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата создания записи')),
                ('updated', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата ред-ия записи')),
            ],
            options={
                'verbose_name': 'О компании',
                'verbose_name_plural': 'О компании',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Название партнера')),
                ('image', models.ImageField(blank=True, upload_to='partners/%Y/%m/%d', verbose_name='Логотип (высота логотипа не должна превышать 40 px!')),
                ('available', models.BooleanField(default=True, verbose_name='Актуальность')),
                ('created', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата создания записи')),
                ('updated', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата ред-ия записи')),
            ],
            options={
                'verbose_name': 'Партнеры',
                'verbose_name_plural': 'Партнеры',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='AboutUsDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(blank=True, default=False, null=True, verbose_name='Главный филиал?')),
                ('is_not_main', models.BooleanField(blank=True, default=True, null=True, verbose_name='Доп. офис')),
                ('available', models.BooleanField(blank=True, default=True, null=True, verbose_name='Активный?')),
                ('address', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Адрес')),
                ('email', models.EmailField(blank=True, default=None, max_length=128, null=True, verbose_name='Емейл')),
                ('phone', models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='Номер тел.')),
                ('schedule_start', models.TimeField(blank=True, null=True, verbose_name='Н. раб. дня (Пн - Пт)')),
                ('schedule_end', models.TimeField(blank=True, null=True, verbose_name='К. раб. дня (Пн - Пт)')),
                ('created', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата создания записи')),
                ('updated', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата ред-ия записи')),
                ('name', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='about_us.AboutUs', verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Подробная информация к компании',
                'verbose_name_plural': 'Подробная информация к компании',
            },
        ),
    ]
