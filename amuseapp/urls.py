# from django.contrib import admin
from django.urls import path, include
from amuseapp import views
from .views import*
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index.html'),
    path('register/',views.register,name='register.html'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('Ticket/',views.Ticket,name='Ticket.html'), 
    path('profile/',views.profile,name='profile'),
    # path('profile/',views.profileupdate,name='profileupdate'),    path('forgot/',views.forgotPassword, name='forgotPassword.html'),
    path('reset/',views.resetPassword,name='reset.html'), 
    path('change_password/', views.change_password, name='change_password'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    #  path('change_password/', views.change_password, name='change_password'),
]