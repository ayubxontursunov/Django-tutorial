from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=250)
    image = models.FileField(upload_to="news_images")

    def __str__(self):
        return self.name
