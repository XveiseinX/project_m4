from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.auth import get_user_model


User = get_user_model()


class Advertisement(models.Model):

    user = models.ForeignKey(
        User,
        verbose_name='пользователь',
        on_delete=models.CASCADE
    )
    
    image = models.ImageField(
        'изображение',
        upload_to = 'advertisements/',
        blank=True,
    )
 
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

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_date = self.created_at.strftime("%H:%M:%S")
            return format_html('<span style="color:green; font-weight:bold;">Сегодня в {} </span>', created_date)
        
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description='Дата изменения')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_date = self.updated_at.strftime("%H:%M:%S")
            return format_html('<span style="color:blue; font-weight:bold;">Сегодня в {} </span>', updated_date)
        
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")
        
    @admin.display(description='Изображение')
    def image_tag(self):
        if self.image:
            return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>', self.image.url)
        else:
            return format_html('<img src="/static/img/adv.png" style="max-width:100px; max-height:100px"/>')
    
    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"   
    
    class Meta:
        db_table = 'advertisements'
    
    # Имя продавца + контакты

    # Актуальность объявления

    # Количество товара

    # Возможен ли обмен

    # Адрес продажи/осмотра

    # Б\У товар или нет

    # Возможность взять в долг в рассрочку 