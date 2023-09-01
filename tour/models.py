from django.db import models
from django.utils.text import slugify
from django.db.models.functions import Coalesce
from datetime import date
from django.db.models import F, Case, When, Value

class Tour(models.Model):
    title = models.CharField(null=True, max_length=50, verbose_name="Назва англійською")
    title1 = models.CharField(null=True, max_length=50, verbose_name="Назва 1 строка")
    title2 = models.CharField(null=True, max_length=50, verbose_name="Назва 2 строка")
    dateStart = models.DateField(null=True, verbose_name="Дата початку туру")
    dateEnd = models.DateField(null=True, blank=True, verbose_name="Дата закінчення туру")
    
    tagline = models.CharField(max_length=55, verbose_name="Слоган для 2 секції")
    description = models.TextField(max_length=1000, verbose_name="Опис для 2 секції")
    image1Section2 = models.ImageField(upload_to="photos/", verbose_name="Зображення 1 для 2 секції")
    image2Section2 = models.ImageField(upload_to="photos/", verbose_name="Зображення 2 для 2 секції")
    image3Section2 = models.ImageField(upload_to="photos/", verbose_name="Зображення 3 для 2 секції")
    
    priceAdult = models.CharField(null=True, blank=True, max_length=15, verbose_name="Ціна для дорослих")
    priceChild = models.CharField(null=True, blank=True, max_length=15, verbose_name="Ціна для дітей")
    dateBeforeAdult = models.DateField(null=True, blank=True, verbose_name="Дата, до якої діє скидка дорослим")
    dateBeforeChild = models.DateField(null=True, blank=True, verbose_name="Дата, до якої діє скидка дітям")
    priceAdultBefore = models.CharField(null=True, blank=True, max_length=15, verbose_name="Ціна для дорослих зі скидкою")
    priceChildBefore = models.CharField(null=True, blank=True, max_length=15, verbose_name="Ціна для дітей зі скидкою")
    
    isActive = models.BooleanField(null=True, default=True, verbose_name="Діючий тур")
    isOutside = models.BooleanField(null=True,default=True, verbose_name="Закордонний тур")
    isOneDay = models.BooleanField(null=True,default=False, verbose_name="Поїздка вихідного дня")
    
    backgroundSection1 = models.ImageField(null=True, upload_to="photos/", verbose_name="Фон першої секції")
    backgroundAdditionalServices = models.ImageField(null=True, upload_to="photos/", verbose_name="Фон секції додаткових послуг")
    backgroundSectionBooking = models.ImageField(null=True, upload_to="photos/", verbose_name="Фон секції забронювати")
    
    ##slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tour, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title1
        
    class Meta:
        ordering = [
            Case(
                When(dateStart=None, then=Value(1)),
                When(dateStart__lt=date.today(), then=Value(2)),
                default=Value(0),
                output_field=models.IntegerField()
            ),
            'dateStart',
        ]
        
class ImageForGalery(models.Model):
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE, null=True, verbose_name="Тур", related_name="images")
    image = models.ImageField(null=True, upload_to='photos/galery', verbose_name="Зображення дня")
    
class Day(models.Model):
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE, null=True, verbose_name="Тур", related_name="days")
    number = models.CharField(null=True, max_length=7, verbose_name="Номер дня (днів)")
    description = models.TextField(null=True, max_length=1500, verbose_name="Опис дня")
    
class ImageForDay(models.Model):
    day = models.ForeignKey('Day', on_delete=models.CASCADE, null=True, verbose_name="День", related_name="images")
    title = models.CharField(null=True, max_length=50, verbose_name="Опис зображення")
    image = models.ImageField(null=True, upload_to='photos/days', verbose_name="Зображення дня")
    
class WhyWe(models.Model):
    title = models.CharField(null=True, max_length=50, verbose_name="Чому ми")
    description = models.TextField(null=True, max_length=1000, verbose_name="Подробно, чому ми")
    icon = models.ForeignKey('Icon', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Іконка")
    
class Inclusive(models.Model):
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE, null=True, verbose_name="Тур")
    title = models.CharField(null=True, max_length=50, verbose_name="Що включено у вартість")
    description = models.TextField(null=True, max_length=1000, verbose_name="Подробний опис")
    icon = models.ForeignKey('Icon', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Іконка")
    
class NotInclusive(models.Model):
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE, null=True, verbose_name="Тур")
    title = models.CharField(null=True, max_length=50, verbose_name="Що входить у вартість")
    description = models.TextField(null=True, max_length=1000, verbose_name="Подробний опис")
    icon = models.ForeignKey('Icon', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Іконка")
    price = models.CharField(null=True, blank=True, max_length=15, verbose_name="Ціна додаткової послуги")
    
class Icon(models.Model):
    title = models.CharField(null=True, max_length=50, verbose_name="Опис зображення")
    icon = models.FileField(null=True, upload_to='photos/icons', verbose_name="Іконка")
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
    
class Review(models.Model):
    name = models.CharField(null=True, max_length=50, verbose_name="Ім'я, Прізвище")
    review = models.TextField(null=True, max_length=1000, verbose_name="Зміст відгуку")
    date = models.DateTimeField(null=True, auto_now_add=True)
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE, null=True, verbose_name="Поїздка, про яку ви хочете залишити відгук")
    
    class Meta:
        ordering = ['-date']
        
class Client(models.Model):
    name = models.CharField(null=True, max_length=50, verbose_name="Ім'я, Прізвище")
    phone = models.CharField(null=True, max_length=20, verbose_name="Номер телефону")
    email = models.EmailField(max_length=254, blank=True, null=True, verbose_name="Електронна пошта")
    permitToEmail = models.BooleanField(default=True, verbose_name="Я хочу отримувати на електронну пошту щодо майбутніх поїздок")
    