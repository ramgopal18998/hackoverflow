import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from myorders.models import Order,Delivery
from user_panel.models import Customer
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers


# this view is the base view


@csrf_exempt		
def index(request):
	if request.method == "GET":
		pending = Order.objects.filter(status=1)
		delivered = Order.objects.filter(status=2)
		return render(request, 'member_panel/member.html',{'pending':pending,'delivered':delivered})
	else:
		bill = request.POST['bill']
		results = Order.objects.filter(bill__startswith=bill,status=1)
		queryset = serializers.serialize('json',results)
		return HttpResponse(queryset,content_type='application/json')

@csrf_exempt
def submit(request):
	if request.method == "POST":
		bill = request.POST.get('bill',False)
		status = request.POST.get('status',False)
		time = request.POST.get('time',False)
		print(str(bill))
		try:
			order = Order.objects.get(bill=bill)
			try:
				delivery = Delivery.objects.get(order_id=order.id,order__status=1)
				delivery.location = status
				delivery.time_left = time
				print("status")
				delivery.save()
				return HttpResponse('success')
			except:
				return HttpResponse('Not yet dispatched')
		except:
			return HttpResponse('error')

@csrf_exempt
def payment(request):
	if request.method == "POST":
		bill = request.POST.get('bill',False)
		try:
			order = Order.objects.get(bill=bill)
			order.status = 2
			order.save()
			return HttpResponse('success')
		except:
			return HttpResponse('error')





