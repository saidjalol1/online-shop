from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_deliver = models.BooleanField(default=False)
    is_warehouseworker = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    

