from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_to_cart/$',views.add_to_cart,name='add_to_cart'),
    url(r'^mycart/$',views.mycart,name='mycart'),
    url(r'^(?P<cart_id>[0-9]+)/cart/delete$',views.delete_from_cart,name='delete_from_cart'),
    url(r'^(?P<p_id>[0-9]+)/view$',views.detail_view,name='detail_view'),
    url(r'^checkout/$',views.checkout,name='checkout'),
    url(r'^buynow/$',views.buynow,name='buynow'),
    url(r'^search/$',views.search,name='search'),
    url(r'^subcategory/(?P<sc_id>[0-9]+)$',views.subcategory_BUY,name='subcategory_BUY'),
]