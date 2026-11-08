from django.urls import path
from . import views

app_name = 'weblog'

urlpatterns = [
path('', views.weblog, name='weblog'),
path('detail/', views.posts, name='posts'),
]