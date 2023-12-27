from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('order_form', views.order_form),
    path('prod_form', views.prod_form),
    path('cust_form', views.cust_form),
]
