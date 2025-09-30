# administration/observers.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Computer, ComputerLog

@receiver(post_save, sender=Computer)
def log_computer_save(sender, instance, created, **kwargs):
    action = "created" if created else "updated"
    ComputerLog.objects.create(computer=str(instance), action=action)

@receiver(post_delete, sender=Computer)
def log_computer_delete(sender, instance, **kwargs):
    ComputerLog.objects.create(computer=str(instance), action="deleted")
