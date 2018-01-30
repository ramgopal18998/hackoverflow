from django.db import models
from django.contrib.auth.models import User



STATUS_CHOICES = (
    ('Customer', 'Customer'),
    ('Member', 'Member'),
    ('SuperAdmin', 'SuperAdmin'),
    )

class Customer(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	FirstName = models.CharField( null=False , max_length=100)
	LastName = models.CharField( null=False , max_length=100)
	address = models.CharField( null=True , max_length=500)
	email = models.CharField( null=False , max_length=500)
	state = models.CharField( null=True , max_length=500)
	mobile = models.CharField( null=False,max_length=10 )
	pin = models.CharField( null=True,max_length=6 )
	image = models.FileField(null=True)
	type = models.CharField(choices=STATUS_CHOICES,max_length=100,null=False,default="Customer")


	def __str__(self):
		return self.FirstName	

	def save(self, *args, **kwargs): 	
	   self.email = self.user.email
	   super(Customer, self).save(*args, **kwargs)



class Review(models.Model):
	customer = models.ForeignKey('Customer',on_delete=models.CASCADE)
	description = models.CharField(max_length=1000,null=False)

	def __str__(self):
		return self.description