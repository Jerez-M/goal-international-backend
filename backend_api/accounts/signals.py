from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .username import get_username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
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
