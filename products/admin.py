from django.contrib import admin
from .models import CategoryData,ProductData,SubCategoryData

# Register your models here.

class SubCategoryDataAdmin(admin.ModelAdmin):
	list_display = ["name","image","category"]
admin.site.register(SubCategoryData,SubCategoryDataAdmin)


class CategoryDataAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "image"]

admin.site.register(CategoryData,CategoryDataAdmin)

class ProductDataAdmin(admin.ModelAdmin):
    list_display = ["name","description","category","image"]

admin.site.register(ProductData,ProductDataAdmin)