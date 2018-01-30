from django.db import models
import user_panel
from smart_selects.db_fields import ChainedForeignKey
import decimal


class CategoryData(models.Model):
	name = models.CharField( null=False , max_length=100)
	description = models.CharField(max_length=500,null=False)
	image = models.FileField()

	def __str__(self):
		return self.name


class SubCategoryData(models.Model):
	name = models.CharField( null=False , max_length=100)
	description = models.CharField(max_length=500,null=False)
	image = models.FileField()
	category = models.ForeignKey(CategoryData,on_delete=models.CASCADE)

	def __str__(self):
		return self.name


STATUS_CHOICES = (
    ('Kg', 'Kg'),
    ('gms', 'gms'),
    ('peices', 'peices'),
    ('packet', 'packet'),
    ('box', 'box'),
    ('Lt', 'Lt'),
    ('ml', 'ml'))




class ProductData(models.Model):
	name = models.CharField(null=False, max_length=500)
	description = models.CharField(max_length=500,null=False)
	category = models.ForeignKey(CategoryData,null=False,on_delete=models.CASCADE)
	image = models.FileField()
	sub_category_name = ChainedForeignKey(SubCategoryData, chained_field="category",
                                          chained_model_field="category", null=True)
	brand = models.CharField(null=True, max_length=100)
	mass = models.DecimalField(null=False,decimal_places=2,max_digits=50,default=1)
	unit = models.CharField(max_length=500, blank=False, null=False, default='Kg', choices=STATUS_CHOICES)
	available = models.BooleanField(default=False)
	price = models.DecimalField(null=True,decimal_places=2,max_digits=50)
	discount_percentage = models.DecimalField(null=True,decimal_places=2,max_digits=50)
	discounted_price = models.DecimalField(null=True,decimal_places=2,max_digits=50)
	reviews = models.ManyToManyField('user_panel.Review',blank=True)

	def __str__(self):
		return self.name
	def save(self, *args, **kwargs):
		x = float(self.price)
		y = float(self.discount_percentage)
		z = x - x*0.01*y
		self.discounted_price = decimal.Decimal(z)
		super(ProductData,self).save(*args, **kwargs)









