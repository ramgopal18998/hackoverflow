from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	FirstName = models.CharField( null=False , max_length=100)
	LastName = models.CharField( null=False , max_length=100)
	address = models.CharField( null=True , max_length=500)
	email = models.CharField( null=False , max_length=500)
	state = models.CharField( null=True , max_length=500)
	mobile = models.CharField( null=False,max_length=10 )
	pin = models.CharField( null=True,max_length=6 )



	def __str__(self):
		return self.FirstName	

	def save(self, *args, **kwargs):
	   self.user.username = self.email
	   self.user.save()
	   super(Customer, self).save(*args, **kwargs)