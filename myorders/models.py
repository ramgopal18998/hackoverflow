from django.db import models
from cart.models import Cart
import user_panel

import random

class Order(models.Model):
	cart = models.ManyToManyField(Cart,blank=True)
	bill = models.CharField(max_length=50,null=False)
	customer = models.ForeignKey("user_panel.Customer",on_delete=models.CASCADE,null=True,default=1)
	grand_total = models.DecimalField(null=True,decimal_places=2,max_digits=50)
	modified = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)
	status = models.IntegerField(null=True,default=0)
	bill_generated = models.BooleanField(default=False)

	def __str__(self):
		return str(self.bill)
	def get_cart(self):
		return "\n".join([str(p) for p in self.cart.all()])

	def save(self, *args, **kwargs):
		super(Order,self).save(*args, **kwargs)
		self.grand_total = 0
		for obj in self.cart.all():
			self.grand_total += obj.total_price
			print("increment ",obj.total_price)
		if not self.bill_generated:
			self.bill = str(random.randint(10000000,99999999)) + str(self.id)
			self.bill_generated = 1
		
			
		super(Order,self).save(*args, **kwargs)




class Delivery(models.Model):
	order = models.ForeignKey('Order',on_delete=models.CASCADE)
	location = models.CharField(max_length=100,null=True)
	time_left = models.CharField(max_length=100,null=True)


