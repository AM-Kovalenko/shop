# Generated by Django 3.2 on 2021-04-26 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_notebook_smartphone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('descriptions', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, max_length=2, verbose_name='Цена')),
                ('fuel_type', models.CharField(max_length=255, verbose_name='Тип топлива')),
                ('brand_name', models.CharField(max_length=255, verbose_name='Производитель')),
                ('model', models.CharField(max_length=255, verbose_name='Модель')),
                ('power', models.CharField(max_length=255, verbose_name='Мощность')),
                ('volume', models.CharField(max_length=255, verbose_name='Объем')),
                ('weight', models.CharField(max_length=255, verbose_name='Масса')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
