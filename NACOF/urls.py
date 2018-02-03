"""NACOF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from user_panel import views


from django.contrib.auth.views import (
    password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^chat/', include('chat.urls')),
    url(r'^user_panel/', include('user_panel.urls')),
    url(r'^member_panel/', include('member_panel.urls')),
    url(r'^products/',include('products.urls',namespace='products')),
    url(r'^cart/',include('cart.urls')),
    url(r'^myorders/',include('myorders.urls')),
    url(r'^login/',views.login_user, name='login'),
    url(r'^register/',views.register_user, name='register'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),

    #reset password
    url(r'^reset-password$',password_reset,{'template_name':'password/reset_password.html','post_reset_redirect':'password_reset_done','email_template_name': 'password/reset_password_email.html'},name='reset_password'),
    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'password/reset_password_done.html'}, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'password/reset_password_confirm.html', 'post_reset_redirect': 'password_reset_complete'}, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete,{'template_name': 'password/reset_password_complete.html'}, name='password_reset_complete'),
    url(r'^$',views.home,name="home"),
]





if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
