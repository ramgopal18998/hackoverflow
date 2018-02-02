from django.shortcuts import render
from .models import Order,Delivery
from cart.models import Cart
from user_panel.models import Review,Customer
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from products.models import ProductData
from django.views.decorators.csrf import csrf_exempt
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf	import pisa
from django.views.generic import View
import decimal


def index(request):
	orders = Order.objects.filter(customer__user_id=request.user.id)
	return render(request,'myorders/index.html',{ "orders":orders })

def detail(request,bill_id):
	order = Order.objects.get(bill=bill_id)
	cart = order.cart.all()
	try:
		delivery = Delivery.objects.get(order__bill=bill_id)
	except:
		return render(request,'myorders/detail.html',{ "order":order,"cart":cart,'delivery':[],'msg':"Not yet dispactched" })

	return render(request,'myorders/detail.html',{ "order":order,"cart":cart,'delivery':delivery })

@csrf_exempt
def review(request,p_id):
	if request.method =='GET':
		return render(request,'myorders/review.html')
	else:
		try:
			review = Review()
			review.description = request.POST.get('review',False)	
			customer = Customer.objects.get(user_id=request.user.id)
			review.customer_id = customer.id
			review.save()
			product = ProductData.objects.get(id=p_id)
			product.reviews.add(review)
			product.save()
			return HttpResponse('success')
		except:
			return HttpResponse('error')


def render_to_pdf(template_src,context_dict={}):
	template = get_template(template_src)
	html = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

class GeneratePDF(View):
	def get(self,request,p_id):
		print(p_id)
		template = get_template("invoice.html")
		order = Order.objects.get(bill=p_id)
		cart = order.cart.all()
		customer = Customer.objects.get(user_id=request.user.id)
		print(customer.id)
		context = {
			"order": order,
			"cart" :cart,
			"customer":customer,
		}
		html = template.render(context)
		pdf = render_to_pdf("invoice.html",context)
		return HttpResponse(pdf,content_type='application/pdf')
@csrf_exempt
def ratings(request):
	if request.method=="POST":
		rating = float(request.POST.get('rating',False))
		pid = request.POST.get('p_id',False)
		try:
			customer = Customer.objects.get(user_id=request.user.id)
			print(customer.id)
			rate = Cart.objects.get(customer_id=customer.id,product_id=pid)
			if rate.rating == '0':
				product = ProductData.objects.get(id=pid)
				star = float(product.stars)
				star += rating
				star = star/2
				print("present ... ",product.stars)
				product.stars = decimal.Decimal(star)
				product.save()
				cart = Cart.objects.get(customer_id=customer.id,product_id=pid)
				cart.rating = rating
				cart.save()
				return HttpResponse("success")
			else:
				return HttpResponse("failed")
		except:
			return HttpResponse("error")


