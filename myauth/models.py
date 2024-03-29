from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify
# Create your models here.

class Profile(models.Model):
    class Meta:
        verbose_name_plural = 'Профили пользователей'
        ordering = ['slug',]
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    choiceuniversity = [
        ('KFU','Казанский Федеральный Университет'),
        ('KAI','Казанский Авиационный Институт'),
        ('КНИТУ','Казанский национальный исследовательский технологический университет'),
        ('КГЭУ','Казанский государственный экономический университет'),
        ('Другой','Нет в списке')
    ]
    university = models.CharField(max_length=255, choices=choiceuniversity, blank = True)
    agreement_accepted = models.BooleanField(default = False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, blank=True, verbose_name="URL")
    def __str__(self):
        return str(self.user)
    

    #Создание slug для аккаунта
    def save(self, *args, **kwargs):
        
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('myauth:profile', kwargs={'slug': self.slug})