from django.db import models


class Cart(models.Model):
    pro_id = models.ForeignKey('product.id', on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey('user.id', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.created_at

