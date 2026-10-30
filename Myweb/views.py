from django.shortcuts import render

# Create your views here.
#صفحه خانه
def home(request):
    return render(request, 'myweb/index.html')

#صفحه درباره ما
def about(request):
    return render(request, 'myweb/about-us.html')


def services(request):
    return render(request, 'myweb/services.html')


def contact(request):
    return render(request, 'myweb/contact.html')


def blog(request):
    return render(request, 'myweb/blog.html')