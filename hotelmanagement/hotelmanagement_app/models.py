from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HotelModel(models.Model):
    Name=models.CharField(max_length=100)
    email=models.EmailField()
    date=models.DateField(auto_now_add=True)
    status=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
