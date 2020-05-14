
from django.urls import path
from order import views

urlpatterns = [
    path('', views.order),
    path('orderview/',views.orderview,name='orderview')
]
