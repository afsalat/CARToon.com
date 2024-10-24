from django.db import models
from product.models import Product
from user.models import customUser


class Cart(models.Model):
    pro_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(customUser, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.created_at

