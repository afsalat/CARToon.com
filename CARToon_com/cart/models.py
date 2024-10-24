from django.db import models
from product.models import Product
from user.models import customUser

class Cart(models.Model):
    pro_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(customUser, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)  # Set a default quantity of 1

    def __str__(self):
        return f"{self.user_id}'s Cart - Product: {self.pro_id} - Quantity: {self.quantity}"
