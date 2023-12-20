from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group

@receiver(post_save, sender=User)
def add_user_to_group(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='user')
        instance.groups.add(group)