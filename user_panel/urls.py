from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.translator, name='translator'),
    url(r'^chatbot/$',views.chatbot,name='chatbot'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^weather_forecast/$',views.weather_forecast,name='weather_forecast'),
    url(r'^questions/$',views.faq,name='faq'),
    url(r'^questions/like$',views.like,name='like'),
    url(r'^questions/dislike$',views.dislike,name='dislike'),
]