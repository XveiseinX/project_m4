from django.db import models


class Advertisement(models.Model):

    # Товар
    # строковое поле для небольших размеров
    # 'заголовок' - verbose_name - название поля извне
    title = models.CharField('Заголовок', max_length=128)

    # Описание товара/информация о товаре
    # большое текстовое поле
    description = models.TextField('описание')

    # Цена
    # специальный тип данных с фиксированной точкой 
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)

    # Уместен ли торг
    # логический тип, два значения правда или ложь
    auction = models.BooleanField('торг', help_text='Отметьте уместность торга')

    # Дата публикации
    # Поле записывается при создании объявления
    created_at = models.DateTimeField(auto_now_add=True)

    # Дата изменения
    # Поле изменяется при каждом обновлении
    updated_at = models.DateTimeField(auto_now=True)
    
    # Имя продавца + контакты

    # Актуальность объявления

    # Количество товара

    # Возможен ли обмен

    # Адрес продажи/осмотра

    # Б\У товар или нет

    # Возможность взять в долг в рассрочку 