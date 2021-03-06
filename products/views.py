from django.shortcuts import render,redirect
from .models import ProductData
from cart.models import Cart
from user_panel.models import Customer
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myorders.models import Order
from django.core import serializers

def index(request):
	products = ProductData.objects.all()
	return render(request,'products/home.html',{'products':products})


@csrf_exempt
def add_to_cart(request):
	p_id = request.POST.get('p_id',False)
	print(p_id)
	customer = Customer.objects.get(user_id=request.user.id)
	# check if product already in cart
	x = Cart.objects.filter(product_id=p_id,customer_id=customer.id,status=0)
	print(len(x))
	if(len(x)):
		return HttpResponse("already in cart")

	# else add product to cart
	cart = Cart()
	cart.customer_id = customer.id 
	cart.product_id = p_id
	cart.save()
	product = ProductData.objects.get(id=cart.product.id)
	print("Added to cart")

	queryset = serializers.serialize('json',[product])
	return HttpResponse(queryset,content_type='application/json')
	

def mycart(request):
	if request.method=="GET":
		customer = Customer.objects.get(user_id=request.user.id)
		items = Cart.objects.filter(customer_id=customer.id,status=0)
		return render(request,'products/cart.html',{'items':items,'customer':customer})


def delete_from_cart(request,cart_id):
	print(cart_id)
	customer = Customer.objects.get(user_id=request.user.id)
	x = Cart.objects.get(id=cart_id,customer_id=customer.id)
	x.delete()
	return redirect('/products/mycart/')

def detail_view(request,p_id):
	print(p_id)
	product = ProductData.objects.get()
	return render(request,"products/detailed_product.html")


@csrf_exempt
def checkout(request):
	ids = list(request.POST.getlist('id[]'))
	quantities = list(request.POST.getlist('quantity[]'))
	for i in range(0,len(ids)):
		cart = Cart.objects.get(id=ids[i])
		cart.quantity = quantities[i]
		cart.save()
	return HttpResponse("success")

@csrf_exempt
def buynow(request):
	address = request.POST.get('address',False)
	customer = Customer.objects.get(user_id=request.user.id)
	carts = Cart.objects.filter(customer_id=customer.id)
	order = Order()
	order.customer_id = customer.id
	order.save()
	gtotal = 0
	for cart in carts:
		cart.status = 1
		cart.save()
		order.cart.add(cart)
		gtotal += cart.total_price
	order.grand_total = gtotal
	
	order.save()
	print("Order saved...")
	return HttpResponse("success")


@csrf_exempt
def search(request):
	query = request.POST['query']
	print(query)
	products = ProductData.objects.filter(name__icontains=query)
	if not len(products):
		products = ProductData.objects.filter(sub_category_name__name__icontains=query)
		if not len(products):
			products = ProductData.objects.filter(category__name__icontains=query)
	products = products[:6]

	queryset = serializers.serialize('json',products)
	print(len(products)," products obtained")
	return HttpResponse(queryset,content_type='application/json')
	
def subcategory_BUY(request,sc_id):
	products = ProductData.objects.filter(sub_category_name__id=sc_id)
	print(len(products) ," found")
	customer = Customer.objects.get(user_id=request.user.id)
	cart = Cart.objects.filter(customer_id=customer.id,status=0)
	return render(request,'products/product_subcategories.html',{'cart':cart,'num':len(cart) ,'products':products})