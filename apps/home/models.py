
from django.db import models


# Create your models here.
class Caritems(models.Model):
    price = models.IntegerField(null=False)
    year = models.IntegerField(null=False)
    km = models.IntegerField(null=False)
    image = models.URLField(max_length=255, null=False)
    url = models.URLField(max_length=255, null=False)
    model = models.CharField(max_length=255, null=False)
    model_type = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.model
