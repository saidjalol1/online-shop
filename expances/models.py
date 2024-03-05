from django.db import models



class Expances(models.Model):
    name = models.CharField(max_length=250)
    amount = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    date_added = models.DateField(auto_now_add = True)


    def __str__(self):
        return self.name
