import json

from django.shortcuts import render
from .models import Message
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from user_panel.models import Customer

# this view is the base view
def chat_index(request):
   customer = Customer.objects.get(user_id=request.user.id)
   print(customer.FirstName)
   context = {
       'messages': Message.objects.all(),
       'username': str(request.user.username),
       'customer': customer
   }
   return render(request, 'chat/chat_whatsapp.html', context)

# this view must be csrf exempted to be able to accept XMLHttpRequests
@csrf_exempt
def save_message(request):
   print(request.user.username)
   if request.method == 'POST':
       msg_obj = json.loads(request.body.decode('utf-8'))
       try:
           msg = Message.objects.create(user_name=msg_obj['user_name'], message=msg_obj['message'])
           msg.save()
       except:
           print("error saving message")
           return HttpResponse("error")
       return HttpResponse("success")
   else:
       return HttpResponseRedirect('/')