from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

# class Billing(models.Model):
#     Price = models.CharField(max_length=10)
#     Fare1 = models.ForeignKey(Punjabi, on_delete=CASCADE)

#     def __str__(self):
#         return self.Price

class Punjabi(models.Model):
    Sabji_Name = models.CharField(max_length=20)
    Price = models.CharField(max_length=10)

    def __str__(self):
        return self.Sabji_Name

class Gujarati(models.Model):
    Sabji_Name = models.CharField(max_length=20)
    Price = models.CharField(max_length=10)

    def __str__(self):
        return self.Sabji_Name

class South_Indian(models.Model):
    Name = models.CharField(max_length=20)
    Price = models.CharField(max_length=10)

    def __str__(self):
        return self.Name

class Italian(models.Model):
    Name = models.CharField(max_length=20)
    Price = models.CharField(max_length=10)

    def __str__(self):
        return self.Name

class Customer(models.Model):
    Name = models.CharField(max_length=50)
    Dish1 = models.ManyToManyField(Punjabi, blank=True)
    Dish2 = models.ManyToManyField(Gujarati, blank=True)
    Dish3 = models.ManyToManyField(South_Indian, blank=True)
    Dish4 = models.ManyToManyField(Italian, blank=True)

    def __str__(self):
        return self.Name

