"""recommend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from user import views as user_view
from products import views as product_view
from recommendation import views as rec_view

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('userview/', user_view.view_list),
    re_path(r'^add/', user_view.add_user),
    re_path(r'^update/(?P<id>\d+)/$', user_view.update_user),
    re_path('productview/', product_view.view_list),
    re_path('productadd/', product_view.add_product),
    re_path(r'^productupdate/(?P<id>\d+)/$', product_view.update_product),
    re_path(r'^productsearch/', product_view.product_search),
    path('logout/', user_view.logout_view),
    path('signup/', user_view.signup_view),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path('recommend/', rec_view.recommend),

]
