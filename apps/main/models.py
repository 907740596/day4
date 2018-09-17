from django.db import models

# Create your models here.
class Img(models.Model):
    img_url=models.CharField(max_length=100)
    type=models.CharField(max_length=30)
    create_date=models.DateTimeField(auto_now_add=True)
    desc=models.CharField(max_length=255)
    class Meta:
        db_table='img'
