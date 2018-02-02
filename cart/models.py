from django.db import models
from django.contrib.auth.models import User
from user_panel.models import Customer
from products.models import ProductData
import decimal
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductData,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1,null=True)
    total_price = models.DecimalField(null=True,decimal_places=2,max_digits=50)
    status = models.BooleanField(default=False)
    rating = models.CharField(default=0,max_length=10)

    def save(self, *args, **kwargs):
    	self.total_price = self.product.discounted_price * decimal.Decimal(self.quantity)
    	super(Cart,self).save(*args, **kwargs)


    def __str__(self):
    	return self.product.name + " " +str(self.total_price)