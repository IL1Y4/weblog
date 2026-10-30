from django.urls import path
from . import views

app_name = 'Myweb'

urlpatterns = [
    path('', views.home , name='home'),
    path('', views.about , name='about'),
    path('', views.contact , name='contact'),
    path('', views.services , name='services'),
    path('', views.blog , name='blog'),
]