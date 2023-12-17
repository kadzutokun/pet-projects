from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from . import models
from django.contrib.auth.models import User
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = 'id','title','price' # Что хотим выводить в админку 
    list_display_links = ["title"] # Что хотим, чтоб было ссылкой на сущность

class OrderAdmin(admin.ModelAdmin):
    list_display = 'id', 'coursetype', 'status', 'user_verbose'
    list_display_links = ['coursetype']
    def user_verbose(self, obj: models.Order) -> str:
        return (obj.user.first_name + ' ' + obj.user.last_name) or obj.user.username
    search_fields = ['coursetype__title','user__last_name','user__first_name']
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return models.Order.objects.select_related('user').prefetch_related('coursetype')

admin.site.register(models.Category)
admin.site.register(models.Course,CourseAdmin)
admin.site.register(models.Order, OrderAdmin)



