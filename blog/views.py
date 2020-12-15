from django.shortcuts import render,HttpResponse
from blog.models import post

# Create your views here.
def blogHome(request):
    allposts= post.objects.all()
    context={'allposts':allposts} 
    return render(request,'blog/blogHome.html',context)
def blogPost(request,slug):
    Post= post.objects.filter(slug=slug).first()
    context={'Post':Post}
    return render(request,'blog/blogPost.html',context)

