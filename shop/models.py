from django.db import models
from crm.models import CustomUser

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
    

class WishlistItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True, verbose_name="Mahsulot")
    session_key = models.CharField(max_length=40,null=True, blank=True)


    def overall_price(self):
        return self.product.price
    

class ProductSold(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True, verbose_name="Mahsulot")
    quantity = models.PositiveBigIntegerField(default=0,verbose_name="Miqdori")
    date_added = models.DateField(auto_now_add = True)


    def overall_price(self):
        return self.product.price * self.quantity
    

class Order(models.Model):
    name = models.CharField(max_length=250, verbose_name="Mijoz Ismi va Familiyasi")
    phone = models.CharField(max_length=20, verbose_name="Mijoz Telefon Raqami")
    region = models.CharField(max_length=250, verbose_name="Viloyat va Tuman")
    street = models.CharField(max_length=250, verbose_name="street")
    target = models.CharField(max_length=250, verbose_name="Mo'ljal")
    date_added = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length=100, default="Active")
    payment_type = models.CharField(max_length=100, verbose_name="To'lov turi", default="Naqd")
    payment_status = models.CharField(max_length=100, verbose_name="To'lov holati", default="Qilinmagan")
    payment_method = models.CharField(max_length=100, default="Naqd")
    payment_deadline = models.DateField(blank=True, null=True)
    deliver = models.ForeignKey(CustomUser, related_name = "orders", blank=True, null=True, on_delete=models.CASCADE)
    barcode_image = models.ImageField(upload_to='barcodes/', null=True, blank=True)


    def overall_price(self):
        return sum([i.get_overall() for i in self.order_items.all() ])
    

class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True, verbose_name="Mahsulot")
    quantity = models.PositiveBigIntegerField(default=0,verbose_name="Miqdori")
    session_key = models.CharField(max_length=40,null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,blank=True,related_name = 'order_items')


    def get_overall(self):
        return self.product.price * self.quantity
    

class Barcode(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    barcode_data = models.CharField(max_length=100, null=True, blank=True)