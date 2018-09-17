from django.db import models

# Create your models here.
class Deng(models.Model):
    name=models.CharField(max_length=64)
    password=models.CharField(max_length=64)
    class Meta:
        db_table="deng"