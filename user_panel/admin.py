from django.contrib import admin
from .models import Customer

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
	list_display = ["FirstName","LastName","mobile","address","email"]
admin.site.register(Customer,CustomerAdmin)


