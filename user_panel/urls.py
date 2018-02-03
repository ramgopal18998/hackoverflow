from django.conf.urls import url

from . import views
app_name='user_panel'
urlpatterns = [
    url(r'^$', views.translator, name='translator'),
    url(r'^chatbot/$',views.chatbot,name='chatbot'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^weather_forecast/$',views.weather_forecast,name='weather_forecast'),
    url(r'^questions/$',views.faq,name='faq'),
    url(r'^questions/like$',views.like,name='like'),
    url(r'^questions/dislike$',views.dislike,name='dislike'),
    url(r'^news$',views.news,name='news'),
    url(r'^(?P<p_id>[0-9]+)question/detail$',views.question_detail,name='question_detail'),

]