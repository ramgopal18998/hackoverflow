from django.contrib import admin
from .models import Cart
class CartAdmin(admin.ModelAdmin):
	list_display = ["customer","product","quantity","total_price","status"]
admin.site.register(Cart,CartAdmin)
