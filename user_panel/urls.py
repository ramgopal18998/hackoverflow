from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.translator, name='translator'),
    url(r'^chatbot/$',views.chatbot,name='chatbot')
]