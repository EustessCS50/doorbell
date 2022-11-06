from django.db import models


# Create your models here.

class Contact(models.Model):
    phone = models.IntegerField()
    email = models.EmailField(default=None)
    address = models.CharField(max_length=100)


class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, default=1)
    password = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='uploads/customers/')

    def __str__(self):
        return self.firstname


class Vendor(models.Model):
    bizname = models.CharField(max_length=50)
    meal = models.CharField(max_length=50)
    location = ()
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, default=1)
    logo = models.ImageField(upload_to='uploads/vendors/')

    def __str__(self):
        return self.name


class Categorie(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, default=1)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/meals/')

    def __str__(self):
        return self.name

#
# from django.db import models
# from django.contrib.auth.models import User
#
#
# # Create your models here.
#
#
# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
#     name = models.CharField(max_length=100, null=True)
#     email = models.CharField(max_length=100, null=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     price = models.FloatField()
#     digital = models.BooleanField(default=False, null=True, blank=False)
#     image = models.ImageField(null=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Order(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False, null=True, blank=False)
#     transaction_id = models.CharField(max_length=100, null=True)
#
#     def __str__(self):
#         return str(self.id)
#
#
# class OrderItems(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
#     quantity = models.IntegerField(default=0, null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)
#
#
# class ShippingAddress(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
#     address = models.CharField(max_length=200, null=True)
#     city = models.CharField(max_length=200, null=True)
#     state = models.CharField(max_length=200, null=True)
#     zipcode = models.CharField(max_length=200, null=True)
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.address
