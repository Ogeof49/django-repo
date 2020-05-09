from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html',
    {'blogs': blogs})
    
def code_auditing(request):
    return render(request, 'services/code_auditing.html')

class BlogDetail(generic.DetailView):
    model = Blog
    template_name = 'repo.html'

