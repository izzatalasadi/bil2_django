from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.home.models import Caritems


@receiver(post_save, sender=Caritems)
def car_saved(sender, instance, created, **kwargs):
    if created:
        print("A new car has been added!")
    else:
        print("An existing car has been updated!")
