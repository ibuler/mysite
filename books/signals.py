from django.db.models.signals import pre_save
from django.core.signals import request_finished
from django.dispatch import receiver


@receiver(pre_save)
def log(sender, **kwargs):
    print("Sender: ")
    print(sender)
    print("Kwargs: ")
    print(kwargs)


@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished")
    print(sender)
    print(kwargs)