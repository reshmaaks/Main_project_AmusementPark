# from django.contrib import admin
from django.urls import path, include
from amuseapp import views
from .views import*
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register.html'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('Ticket/',views.Ticket,name='Ticket.html'), 
    path('profile/',views.profile,name='profile'),
    path('bookticket/',views.bookticket,name='bookticket'),
    path('review/', views.review, name='review'),
    path('profile/update/',views.profile_update,name='profileupdate'),
    path('reset/',views.resetPassword,name='reset.html'), 
    path('change_password/', views.change_password, name='change_password'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('booknow/',views.booknow,name='booknow'),
    path('service/',views.service,name='service'),
    path('Delete/<int:id>/',views.Delete,name='Delete'),
    path('checkout/',views.checkout.as_view(),name='checkout'),
    path('payments/',views.payments,name='payments'),
    path('status/',views.pay,name='status'),
    path('foodlogin/', views.foodlogin, name='foodlogin'),
    path('foodreg/', views.foodreg, name='foodreg'),
    path('home1/', views.home1, name='home1'),
    path('foodlogout/',views.foodlogout, name='foodlogout'),




]