from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),                      # صفحه اصلی (آدرس خالی)
    path('about/', views.about, name='about'),              # صفحه درباره ما
    path('contact/', views.contact, name='contact'),        # صفحه تماس با ما
    path('services/', views.services, name='services'),     # صفحه خدمات
    path('blog/', views.blog, name='blog'),                 # صفحه وبلاگ
]