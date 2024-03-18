# Generated by Django 5.0.3 on 2024-03-18 17:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=255, unique=True, verbose_name='Ссылка')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('producer', models.CharField(max_length=200)),
                ('diagonal', models.CharField(max_length=100)),
                ('resolution', models.CharField(max_length=100)),
                ('os', models.CharField(max_length=100)),
                ('processor', models.CharField(max_length=100)),
                ('ram', models.CharField(max_length=100)),
                ('video_card', models.CharField(max_length=100)),
                ('hdd_type', models.CharField(max_length=100)),
                ('hdd_volume', models.CharField(max_length=100)),
                ('battery', models.CharField(max_length=100)),
                ('condition', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Ноутбук',
                'verbose_name_plural': 'Ноутбуки',
                'db_table': 'Сводка по ноутбукам',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(max_length=255, unique=True)),
                ('notebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product_app.notebook')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
