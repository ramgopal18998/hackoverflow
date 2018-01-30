from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^track_update$', views.submit, name='submit'),
    url(r'^payment$', views.payment, name='submit'),
    
    # url used to process the xmlhttprequests done by nodejs socket.io
    
]