from django.shortcuts import render

# Create your views here.
def weblog(request):
    return render(request, 'weblog/blog.html')

def posts(request):
    return render(request, 'weblog/single-blog.html')