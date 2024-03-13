# yourapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from .models import Notification
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')






def send_notification_to_admin(order_instance):
    notification = Notification.objects.create(
        order = order_instance,
        message=f'Yangi Buyurtma ID-{order_instance.id}.'
    )
    channel.basic_publish(exchange='',
                      routing_key='hello',
                      body= notification.message)


@receiver(post_save, sender=Order)
def notify_admin_on_new_order(sender, instance, created, **kwargs):
    if created:
        send_notification_to_admin(instance)





def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)