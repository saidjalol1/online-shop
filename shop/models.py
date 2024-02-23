from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nomi")
    slug = models.SlugField(max_length=40,unique=True)
    

    def __str__(self):
        return str(self.name)
    

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nomi")
    image = models.ImageField(upload_to="mahsulotlar/",null=True)
    amount = models.CharField(max_length=100, verbose_name="Miqdori")
    price = models.PositiveBigIntegerField(default=0, verbose_name="Narxi")
    description = models.CharField(max_length=300, verbose_name="Tavsifi")
    discount = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan_sanasi")
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,related_name="products", verbose_name="kategoriyasi")


    def __str__(self):
        return str(self.name + " " + self.category.name)
    

class CartItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True, verbose_name="Mahsulot")
    quantity = models.PositiveBigIntegerField(default=0,verbose_name="Miqdori")
    session_key = models.CharField(max_length=40,null=True, blank=True)


    def overall_price(self):
        return self.product.price * self.quantity
