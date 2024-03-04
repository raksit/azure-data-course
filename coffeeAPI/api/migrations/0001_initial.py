# Generated by Django 2.1.15 on 2024-03-04 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CafeLocation',
            fields=[
                ('storeID', models.AutoField(primary_key=True, serialize=False)),
                ('storeName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CafeSales',
            fields=[
                ('TransactionID', models.AutoField(primary_key=True, serialize=False)),
                ('TransactionDate', models.CharField(max_length=255)),
                ('TransactionTime', models.CharField(max_length=255)),
                ('TransactionQty', models.CharField(max_length=255)),
                ('StoreID', models.CharField(max_length=255)),
                ('StoreLocation', models.CharField(max_length=255)),
                ('ProductID', models.CharField(max_length=255)),
                ('UnitPrice', models.CharField(max_length=255)),
                ('ProductCategory', models.CharField(max_length=255)),
                ('ProductName', models.CharField(max_length=255)),
                ('ProductDetail', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CoffeeAndCode',
            fields=[
                ('CodeId', models.AutoField(primary_key=True, serialize=False)),
                ('CodingHours', models.CharField(max_length=255)),
                ('CoffeeCupsPerDay', models.CharField(max_length=255)),
                ('CoffeeTime', models.CharField(max_length=255)),
                ('CodingWithoutCoffee', models.CharField(max_length=255)),
                ('CoffeeType', models.CharField(max_length=255)),
                ('CoffeeSolveBugs', models.CharField(max_length=255)),
                ('Gender', models.CharField(max_length=255)),
                ('Country', models.CharField(max_length=255)),
                ('AgeRange', models.CharField(max_length=255)),
            ],
        ),
    ]