import uuid
from django.db import models


# Create your models here.

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_sku = models.CharField(max_length=50)
    item_name = models.CharField(max_length=200)
    item_quantity = models.PositiveIntegerField()
    current_item_quantity = models.PositiveIntegerField()
    minimum_item_quantity = models.PositiveIntegerField()
    desired_item_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.item_name
    
class Inventory_Items(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    inventory_serial =models.