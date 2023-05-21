from datetime import datetime
from django.db import models


# Create your models here.
class Ideas(models.Model):
    title = models.CharField('Наименование идеи', max_length=255)
    description = models.TextField('Описание текущей ситуации (недостатки)')
    offer = models.TextField('Предложение по улучшению (описание инициативы)')
    effect = models.TextField('Ожидаемый результат')
    economic = models.BooleanField('Экономический эффект', default=False)
    date = models.DateField('Дата публикации', default=datetime.now())

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Идея'
        verbose_name_plural = 'Идеи'
