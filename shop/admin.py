from django.contrib import admin

from . import models


admin.site.register(models.Product)
admin.site.register(models.CartItems)
admin.site.register(models.WishlistItem)
admin.site.register(models.ProductSold)

@admin.register(models.Category)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':('name', )}

