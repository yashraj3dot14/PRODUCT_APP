from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.form, name= 'user_reg'),
    path('login/',views.signin, name = 'user_login'),
]