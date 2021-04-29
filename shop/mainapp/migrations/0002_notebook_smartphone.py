# Generated by Django 3.2 on 2021-04-26 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('descriptions', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, max_length=2, verbose_name='Цена')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Диагональ')),
                ('display', models.CharField(max_length=255, verbose_name='Дисплей')),
                ('resolution', models.CharField(max_length=255, verbose_name='Разрешение экрана')),
                ('accum_volume', models.CharField(max_length=255, verbose_name='бъем батареии')),
                ('ram', models.CharField(max_length=255, verbose_name='ОЗУ')),
                ('sd', models.BooleanField(default='True')),
                ('sd_volume_max', models.CharField(max_length=255, verbose_name='Макс объем встр памяти')),
                ('main_cam_np', models.CharField(max_length=255, verbose_name='Главная камера')),
                ('frontal_cam_np', models.CharField(max_length=255, verbose_name='Фронтальная камера')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('descriptions', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, max_length=2, verbose_name='Цена')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Диагональ')),
                ('display', models.CharField(max_length=255, verbose_name='Дисплей')),
                ('Processor_freq', models.CharField(max_length=255, verbose_name='Частота процессора')),
                ('ram', models.CharField(max_length=255, verbose_name='ОЗУ')),
                ('video', models.CharField(max_length=255, verbose_name='видеокарта')),
                ('time_without_charge', models.CharField(max_length=255, verbose_name='время без зарядки')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]