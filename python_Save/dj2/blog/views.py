from django.shortcuts import render
from blog.models import Blog

# Create your views here.
def archive(request):
    posts = Blog.objects.all()
    return render(request,'archive.html', {'posts':posts})
def home(request):
    posts = Blog.objects.all()
    return render(request,'home.html',{'posts':posts})
def index(request):
    posts = Blog.objects.all()
    return  render(request,'index.html', {'posts':posts})
def article_page(request,posts_id):
    posts = Blog.objects.get(pk=posts_id)
    return  render(request,'article_page.html', {'posts':posts})