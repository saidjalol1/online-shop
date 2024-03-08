from django.db import models
from crm.models import CustomUser
from shop.models import Product


class SailItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True, verbose_name="Mahsulot")
    quantity = models.PositiveBigIntegerField(default=0,verbose_name="Miqdori")
    user = models.ForeignKey(CustomUser,blank=True, on_delete=models.DO_NOTHING, related_name="sail_items")


    def overall_price(self):
        return self.product.price * self.quantity
