from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Property(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    property_name = models.CharField(max_length=50)
    date_of_purchase=models.DateField(auto_now_add=True)
    date_of_addition=models.DateField(auto_now_add=True)
    address = models.CharField(max_length=255)
    def __sre__(self):
        return self.property_name