from django.contrib import admin
from . import models
from django.contrib.auth.models import User
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = 'slug', # Что хотим выводить в админку 
    list_display_links = ['slug'] # Что хотим, чтоб было ссылкой на сущность
    #prepopulated_fields = {"slug": ('user',)}
    def user_verbose(self, obj: models.Profile) -> str:
        return obj.user.username
admin.site.register(models.Profile,ProfileAdmin)
