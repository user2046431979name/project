from django.shortcuts import render
from .models import *
from django.views.generic import ListView,DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView



def index(request):
    return render(request,'index.html')



class contact(CreateView):
    model = Contact
    template_name = 'contact.html'
    fields = ['firstname', 'lastname', 'number','email','message']


def about(request):
    workers = Workers.objects.all()
    reviews = Reviews.objects.all()[:8]
    context = {
        'workers':workers,
        'reviews':reviews
    }
    return render(request,'about.html',context)
def blog(request):
    rows = Blogs.objects.all()
    
    
    context = {
        'rows':rows
    }
    return render(request,'blog.html',context)