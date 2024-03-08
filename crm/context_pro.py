from django.conf import settings
from shop.models import Notification

def notifications(request):
    try:
        notification = Notification.objects.filter(order__status="Active")
    except Notification.DoesNotExist:
        notification = ""
    return {
        'notifications': notification,
    }