from django.urls import path
from . import views

app_name = 'weblog'

urlpatterns = [
path('', views.post_list, name='list'),
path('detail/', views.post_detail, name='detail'),
]