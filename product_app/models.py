from django.db import models

class Notebook(models.Model):
    '''Ноутбуки'''

    link = models.CharField(max_length=255, unique=True, verbose_name='Ссылка')
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    producer = models.CharField(max_length=200)
    diagonal = models.CharField(max_length=100)
    resolution = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    video_card = models.CharField(max_length=100)
    hdd_type = models.CharField(max_length=100)
    hdd_volume = models.CharField(max_length=100)
    battery = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'
        db_table = 'Сводка по ноутбукам'

    def __str__(self):
        return f'{self.title} | {self.price}'


class Image(models.Model):
    """Изображения"""

    image = models.URLField(max_length=255, unique=True)
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE, related_name='images')


    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


    def __str__(self):
        return self.image


