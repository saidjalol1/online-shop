# yourapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from .models import Notification




def send_notification_to_admin(order_instance):
    Notification.objects.create(
        order = order_instance,
        message=f'Yangi Buyurtma ID-{order_instance.id}.'
    )


@receiver(post_save, sender=Order)
def notify_admin_on_new_order(sender, instance, created, **kwargs):
    if created:
        send_notification_to_admin(instance)