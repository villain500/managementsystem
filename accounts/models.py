from django.db import models

# Create your models here.
class Customer(models.Model):
    Name=models.CharField(max_length=200,null=True)
    Phone=models.CharField(max_length=200, null=True)
    Email=models.CharField(max_length=200, null=True)
    Date_Created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.Name
    


class Tag(models.Model):
    Name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.Name
    

class Product(models.Model):
    CATEGORY=(
        ('indoor','indoor'),
        ('out door','out door')
    )
    Name=models.CharField(max_length=200,null=True)
    price=models.IntegerField(default=None)
    category=models.CharField(max_length=200,null=True, choices=CATEGORY)
    description=models.CharField(max_length=200,null=True)
    Date_Created=models.DateTimeField(auto_now_add=True,null=True)
    tags=models.ManyToManyField(Tag)

    def __str__(self):
        return self.Name



class Order(models.Model):

    STATUS=(
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered')
    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    Date_Created=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=200,null=True, choices=STATUS)

    def __str__(self):
        return self.product.Name
    