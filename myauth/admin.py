from django.contrib import admin
from . import models
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = 'id','university','agreement_accepted','user_id' # Что хотим выводить в админку 
    list_display_links = ["id"] # Что хотим, чтоб было ссылкой на сущность
admin.site.register(models.Profile)
