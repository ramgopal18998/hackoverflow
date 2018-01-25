from django.db import models
from smart_selects.db_fields import ChainedForeignKey

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


class ProductData(models.Model):
	name = models.CharField(null=False, max_length=500)
	description = models.CharField(max_length=500,null=False)
	category = models.ForeignKey(CategoryData,null=False,on_delete=models.CASCADE)
	image = models.FileField()
	sub_category_name = ChainedForeignKey(SubCategoryData, chained_field="category",
                                          chained_model_field="category", null=True)

    
