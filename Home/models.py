from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    Name = models.CharField(max_length=30)
    Description = models.TextField()
    def __str__(self):
        return self.Name
class Vests(models.Model):
    Name = models.CharField(max_length=40)
    Price = models.IntegerField(blank=True, null = True)
    CategoryID = models.ForeignKey(Category, default=None, on_delete=models.CASCADE, blank=True, null = True)
    NumberBuy = models.IntegerField(blank=True, null = True)
    Made_in = models.CharField(max_length=40)
    Sales = models.BooleanField(null= False, blank=False)
    New_Price = models.IntegerField(blank=True, null = True)
    Image = models.ImageField()
    Description = models.TextField(blank=True, null = True)
    def __str__(self):
        return self.Name
class CartUser(models.Model):
    VestsID = models.ForeignKey(Vests, default=None, on_delete=models.CASCADE, blank=True, null = True)
    Quantity = models.IntegerField(blank=True, null = True)
    UserID = models.ForeignKey(User, default=None, on_delete=models.CASCADE, blank=True, null = True)
class BillUser(models.Model):
    Date = models.DateTimeField(auto_now_add = True)
    UserID = models.ForeignKey(User, default=None, on_delete=models.CASCADE, blank=True, null = True)
    Image = models.ImageField()
    Ship = models.BooleanField(null= True, blank=True)
class UserInformation(models.Model):
    UserID = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    Phone = models.IntegerField(blank=True, null = True)
    Height = models.IntegerField(blank=True, null = True)
    Weight = models.IntegerField(blank=True, null = True)
    DOB = models.DateTimeField()
    Gender = models.CharField(max_length=40)
