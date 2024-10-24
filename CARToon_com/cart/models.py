from django.db import models


class Cart(models.Model):
    pro_id = models.IntegerField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user_id}'s Cart - Product: {self.pro_id} - Quantity: {self.quantity}"
