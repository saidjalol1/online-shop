from django.contrib import admin

from . import models


admin.site.register(models.Seller)
admin.site.register(models.Deliver)
admin.site.register(models.WareHouseWorker)
