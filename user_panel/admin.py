from django.contrib import admin
from .models import Customer,Review,Weather

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
	list_display = ["FirstName","LastName","mobile","address","email"]
admin.site.register(Customer,CustomerAdmin)


class ReviewAdmin(admin.ModelAdmin):
	list_display = ["description","customer"]
admin.site.register(Review,ReviewAdmin)

class WeatherAdmin(admin.ModelAdmin):
	list_display = ["type","image"]
admin.site.register(Weather,WeatherAdmin)
