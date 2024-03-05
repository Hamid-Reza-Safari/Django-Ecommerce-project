from django.db import models
from decimal import Decimal
import datetime



# Products category
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'


class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0 ,max_digits=100, decimal_places=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , default=1)
    description = models.TextField(max_length=2000 , default='', blank = True , null = True)
    image = models.ImageField(upload_to='uploads/product/', blank=True)
    image2 = models.ImageField(upload_to='uploads/product/', blank=True)
    image3 = models.ImageField(upload_to='uploads/product/', blank=True)
    image4 = models.ImageField(upload_to='uploads/product/', blank=True)
    # discount stuff (takhfif)
    discount = models.BooleanField(default=False)
    sale_discount = models.DecimalField(default=0 ,max_digits=3, decimal_places=0 , blank = True , null = True)
    
    def discounted_price(self):
        if self.discount:
            discount_amount = (self.price * self.sale_discount) / 100
            discounted_price = self.price - discount_amount
            return "{:,}".format(discounted_price)
        else:
            return self.price

        
    def formatted_price(self):
    # Convert the price to a string and add commas for thousands separator
        return "{:,}".format(self.price)
    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=200, default='' , blank = True , null = True)
    phone = models.CharField(max_length=10 , default='' , blank = True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.product