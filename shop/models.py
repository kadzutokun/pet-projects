from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


def product_image_directory(instance: "Course", filename: str) -> str:
    return "products/product_{title}/preview/{filename}".format(
        title = instance.title,
        filename = filename,
    )

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Категории товаров'
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Course(models.Model):
    class Meta:
        ordering = ['title'] # Сортировка по полю title
        verbose_name_plural = "Товары" # Указание как будет выглядить во мн.ч

    title = models.CharField(max_length=255)
    about = models.TextField(null=False, blank=True)
    price = models.IntegerField()
    check_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    preview = models.ImageField(null = True, blank = True, upload_to = product_image_directory)

    def __str__(self):
        return self.title
    
class Order(models.Model):
    class Meta:
        verbose_name_plural = 'Заказы'
    choicesorderstatus = [
        ('Accepted','Заказ принят'),
        ('paid','Заказ оплачен'),
        ('in work','Выполняется'),
        ('comleted','Выполнен'),
    ]
    coursetype = models.ForeignKey(Course, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")
    status = models.CharField(max_length=255, choices=choicesorderstatus)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    receipt = models.FileField(null = True, upload_to = 'orders/receipts/')

class Comment(models.Model):
    class Meta:
        verbose_name_plural = 'Комментарии'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coursecom = models.ForeignKey(Course, on_delete = models.CASCADE)
    commenttext = models.TextField(null = False, blank = False)
    parent_id = models.IntegerField(null = True, blank = True) 
    
    def __str__(self):
        return self.commenttext
