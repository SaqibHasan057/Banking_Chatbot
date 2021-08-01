from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('balanceInquiry', views.balanceInquiry, name='balanceInquiry'),
    path('creditCardInquiry', views.creditCardInquiry, name='creditCardInquiry'),
    path('lastTransaction', views.lastTransaction, name='lastTransaction'),
    path('sendMoney', views.sendMoney, name='sendMoney')
]