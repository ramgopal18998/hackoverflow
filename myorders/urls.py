from django.conf.urls import url
app_name = 'myorders'

from . import views
from .views import GeneratePDF

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<bill_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^(?P<p_id>[0-9]+)/review$', views.review, name='review'),
	url(r'^(?P<p_id>[0-9]+)/invoice$', GeneratePDF.as_view(), name='invoice'),
    
    
    # url used to process the xmlhttprequests done by nodejs socket.io
    
]