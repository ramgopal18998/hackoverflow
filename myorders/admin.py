from django.contrib import admin
from .models import Order,Delivery
class OrderAdmin(admin.ModelAdmin):
	list_display = ["id","get_cart","bill","grand_total","created","modified","status"]
admin.site.register(Order,OrderAdmin)




class DeliveryAdmin(admin.ModelAdmin):
	list_display = ["order","location","time_left"]
admin.site.register(Delivery,DeliveryAdmin)