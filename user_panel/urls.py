
from django.conf.urls import url

from . import views
app_name = "user_panel"

urlpatterns = [
    url(r'^$', views.translator, name='translator'),
    url(r'^chatbot/$',views.chatbot,name='chatbot'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^weather_forecast/$',views.weather_forecast,name='weather_forecast'),
    url(r'^questions/$',views.faq,name='faq'),
    url(r'^questions/like$',views.like,name='like'),
    url(r'^questions/dislike$',views.dislike,name='dislike'),
    url(r'^news$',views.news,name='news'),
    url(r'^maps$',views.maps,name='maps'),
    url(r'^organic$',views.organic,name='organic'),
    url(r'^organic/compost$',views.compost,name='compost'),
    url(r'^organic/manure$',views.manure,name='manure'),
    url(r'^organic/marketing$',views.marketing,name='marketing'),
    url(r'^organic/practices$',views.practices,name='practices'),
    url(r'^organic/protection$',views.protection,name='protection'),
    url(r'^organic/pst$',views.pst,name='pst'),
    url(r'^calculator$',views.calculator,name='calculator'),
    
    url(r'^info_portal$',views.info_portal,name='info_portal'),
    url(r'^(?P<p_id>[0-9]+)question/detail$',views.question_detail,name='question_detail'),


]