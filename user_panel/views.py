from django.shortcuts import render,redirect
from translator import get_in_hindi,get_utube
import wikipedia
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from myorders.models import Order
from . models import Customer
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from products.models import ProductData
from django.conf import settings
import urllib3
from urllib.request import urlopen 
import urllib
import json
from django.contrib.auth import authenticate, login
import codecs
from weather import get_weather,getCity
import pytemperature
from products.tokens import account_activation_token
from user_panel.models import Weather
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text


def translator(request):
	
	print(request.user)
	text = "1. Organic manures produce optimal condition in the soil for high yields and good quality crops2. They supply the entire nutrient required by the plant (NPK, secondary and micronutrients).3. They improve plant growth and physiological activities of plants"

	text = get_in_hindi(text)
	return render(request,'user_panel/translate.html',{ "text":text })



@csrf_exempt
def chatbot(request):
	if request.method == "GET":
		print(str(request.user.email))
		customer = Customer.objects.get(email=str(request.user.email))
		return render(request,'user_panel/chatbot.html',{'customer':customer})
	else:
		print("post request wikipeida")
		query_obj = json.loads(request.body.decode('utf-8'))
		text = str(query_obj['query'])
		url = get_utube(text)
		results = {}
		try:
			results = wikipedia.summary(text,sentences=5)
			results = { "english":results,"hindi":get_in_hindi(results),"url":url }
		except:
			print("wikipedia failed to saerch")
			results["english"] = "Not found anything"
			results["hindi"] = get_in_hindi(results["english"])
			results["url"] = url

		
		return JsonResponse(results)

def login_user(request):
	if request.method == "GET":
		return render(request,'user_panel/login.html')
	else:
		recaptcha_response = request.POST.get('g-recaptcha-response')
		url = 'https://www.google.com/recaptcha/api/siteverify'
		values = {
		    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
		    'response': recaptcha_response
		}
		data = urllib3.request.urlencode(values).encode("utf-8")
		req = urllib.request.Request(url, data)
		response = urlopen(req)
		reader = codecs.getreader("utf-8")
		result = json.load(reader(response))
		if 1:#result['success']
			email = request.POST['username']
			print(email)
			password = request.POST['password']
			user = User.objects.get(email=email)
			print(user.id)
			user = authenticate(username=user.username, password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					customer = Customer.objects.get(user_id=request.user.id)
					if customer.type == "Member":
						return redirect('/member_panel')
					else:
						return redirect('/products')
				else:
					return render(request, 'user_panel/login.html', {'error_message': 'Your account has been disabled'})

			else:
				return render(request, 'user_panel/login.html', {'error_message': 'Invalid login'})
		else:
			return render(request, 'user_panel/login.html', {'error_message': 'Invalid reCAPTCHA. Please try again.'})


def profile(request):
	city = 'bilaspur'
	results = get_weather(city)
	date = results['query']['results']['channel'][0]['item']['condition']['date']
	temp = pytemperature.f2c(int(results['query']['results']['channel'][0]['item']['condition']['temp']))
	text = results['query']['results']['channel'][0]['item']['condition']['text']
	weather_img = Weather.objects.get(type=text)
	weather = {}
	weather['date'] = date
	weather['temp'] = temp
	weather['text'] = text
	return render(request,'user_panel/profile.html',{'weather':weather,'weather_img':weather_img})


@csrf_exempt
def weather_forecast(request):
	city = 'raigarh'
	print("City detected : ",city)
	results = get_weather(city)
	forecast = []
	for i in range(0,10):
		entry = {}
		entry['high'] = results['query']['results']['channel'][i]['item']['forecast']['high']
		entry['low'] = results['query']['results']['channel'][i]['item']['forecast']['low']
		entry['text'] = results['query']['results']['channel'][i]['item']['forecast']['text']
		entry['day'] = results['query']['results']['channel'][i]['item']['forecast']['day']
		entry['date'] = results['query']['results']['channel'][i]['item']['forecast']['date']
		text = results['query']['results']['channel'][i]['item']['forecast']['text']
		try:
			weather_img = Weather.objects.get(type=text)
		except:
			print("not for : ",text)	
		entry['image'] = weather_img.image
		forecast.append(entry)

	#print(forecast)
	return render(request,'user_panel/weather_forecast.html',{'forecast':forecast})

@csrf_exempt
def register_user(request):
	if request.method =='GET':
		return render(request,'user_panel/register.html')

	else:
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		address = request.POST['address']
		city = request.POST['city']
		mobile = request.POST['mobile']
		password = request.POST['password']
		pin = request.POST['pincode']
		image = request.FILES.get('image',False)
		user = User()
		user.username = first_name
		user.set_password(password)
		user.email = email
		user.is_active = False
		user.save()
		current_site = get_current_site(request)
		mail_subject = 'Activate your blog account'
		message = render_to_string('confirm_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
		to_email = email
		email1 = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
		email1.send()
		return HttpResponse('Please confirm your email address to complete the registration')
		# customer = Customer()
		# user1 = User.objects.get(username=first_name)
		# customer.user_id = user1.id
		# customer.FirstName = first_name
		# customer.LastName = last_name
		# customer.mobile = mobile
		# customer.address = address
		# customer.pin = pin
		# customer.city = city
		# customer.email = email
		# customer.image = image
		# customer.save()
		# #send email
		# subject = 'You have successfully registered'
		# message = 'hey '+ user1.username +', your account has been registered successfully.'
		# from_email = settings.EMAIL_HOST_USER
		# to_list = [user.email,settings.EMAIL_HOST_USER]
		# send_mail(subject,message,from_email,to_list,fail_silently = True)
		# return redirect('/products')
		
def activate(request,uidb64,token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
        # return redirect('home')
		return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
	else:
		return HttpResponse('Activation link is invalid!')




