from django.db import models

# Create your models here.


class CafeSales(models.Model):
    TransactionID = models.AutoField(primary_key=True)
    TransactionDate = models.CharField(max_length=255)
    TransactionTime = models.CharField(max_length=255)
    TransactionQty = models.CharField(max_length=255)
    StoreID = models.CharField(max_length=255)
    StoreLocation = models.CharField(max_length=255)
    ProductID = models.CharField(max_length=255)
    UnitPrice = models.CharField(max_length=255)
    ProductCategory = models.CharField(max_length=255)
    ProductName = models.CharField(max_length=255)
    ProductDetail = models.CharField(max_length=255)


class CoffeeAndCode(models.Model):
    CodeId = models.AutoField(primary_key=True)
    CodingHours = models.CharField(max_length=255)
    CoffeeCupsPerDay = models.CharField(max_length=255)
    CoffeeTime = models.CharField(max_length=255)
    CodingWithoutCoffee = models.CharField(max_length=255)
    CoffeeType = models.CharField(max_length=255)
    CoffeeSolveBugs = models.CharField(max_length=255)
    Gender = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    AgeRange = models.CharField(max_length=255)


class CafeLocation(models.Model):
    storeID = models.AutoField(primary_key=True)
    storeName = models.CharField(max_length=255)
