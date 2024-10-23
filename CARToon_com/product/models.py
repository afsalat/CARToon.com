from django.db import models


class Product(models.Model):
    pro_name = models.CharField(max_length=250)
    pro_decription = models.TextField()
    pro_price = models.IntegerField()
    pro_image = models.ImageField(upload_to='../static/imgProducts/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pro_name