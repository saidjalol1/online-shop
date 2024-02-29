from django.db import models
from django.contrib.auth.models import User



class WareHouseWorker(User):
    is_warehouseworker = models.BooleanField(default=True)
    salary = models.BigIntegerField(default=0)
    position = models.CharField(max_length=20, default="ombor xodimi")

    class Meta:
        verbose_name = 'Warehouse Worker'
        verbose_name_plural = 'Warehouse Workers'

    def __str__(self):
        return str(self.username + " " + self.position)


class Seller(User):
    is_seller = models.BooleanField(default=True)
    salary = models.BigIntegerField(default=0)
    position = models.CharField(max_length=20, default="sotuvchi")

    class Meta:
        verbose_name = 'Seller'

    def __str__(self):
        return str(self.username + " " + self.position)


class Deliver(User):
    is_deliver = models.BooleanField(default=True)
    salary = models.BigIntegerField(default=0)
    position = models.CharField(max_length=20, default="Yetkazib beruvchi")

    class Meta:
        verbose_name = 'Deliver'

    def __str__(self):
        return str(self.username + " " + self.position)
