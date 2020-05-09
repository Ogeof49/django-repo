from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html',
    {'blogs': blogs})

def web_design(request):
    return render(request, 'services/web_design.html')

def graphics_design(request):
    return render(request, 'services/graphics_design.html')

def code_auditing(request):
    return render(request, 'services/code_auditing.html')
    
def photography(request):
    return render(request, 'services/photography.html')

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/index.html',
    {'blogs': blogs})

def about(request):
    abouts = Blog.objects.all()
    return render(request, 'about/index.html',
    {'abouts': abouts})
        
def contact(request):
    contacts = Blog.objects.all()
    return render(request, 'contact/index.html',
    {'contacts': contacts})


class BlogDetail(generic.DetailView):
    model = Blog
    template_name = 'repo.html'

