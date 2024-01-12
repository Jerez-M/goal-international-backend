from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .username import get_username
from accounts.models import User


@receiver(post_save, sender=User)
def user_save_handler(sender, instance, created, **kwargs):
    if created:
        if instance.organisation_id is None:
            instance.username = get_username()
            instance.save()
        else:
            instance.username = get_username(
                organisation=instance.organisation_id
            )
            instance.save()

# @receiver(post_save, sender=User)
# def update_username(sender, instance, created, **kwargs):
#     if created:
#         # Generate the initial username on creation
#         instance.username = get_username(instance.organisation_code)
#         instance.save()