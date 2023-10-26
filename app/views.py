from django.shortcuts import render
from .models import *
from django.views.generic import ListView,DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.core.paginator import Paginator


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["category_data"] = {}

        categories = Category.objects.all()[:6]
        for category in categories:
            products = Products.objects.filter(categoryObject=category)[:10]
            context["category_data"][category] = products

        return context  
        

def productsDetails(request,id):
    row = Products.objects.get(id = id)
    images = ProductsImages.objects.filter(productObject = row)
    context = {
        'row':row,
        'images':images
    }
    return render(request,'product-details.html',context)
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
    paginator = Paginator(rows, 3)
   
    page_number = 1
    if request.GET.get('page'):
        page_number = int(request.GET.get('page'))

    next_page = page_number + 1 if (page_number) < len(paginator.page_range) else 1

    previos_page = page_number - 1 if (page_number - 1) != 0 else page_number
    context = {
        'rows':paginator.page(page_number),
        'pages':paginator.page_range,
        'nextP':next_page,
        'previosP':previos_page,
    }
    return render(request,'blog.html',context)


def shopPage(request):
    page = 1
    
    
    if request.GET.get('page'):
        page = int(request.GET.get('page'))
    
    products = Products.objects.all()
    paginator = Paginator(products,2)
    next_page = page + 1 if (page) < len(paginator.page_range) else 1
    previos_page = page - 1 if (page - 1) != 0 else page
    old_price = Products.objects.annotate(old_price=F('price') + F('price') * 0.2)
   
    
    context = {
        'products':paginator.page(page),
        'page':paginator.page_range,
        'nextP':next_page,
        'previosP':previos_page,
        'old_price':old_price    
    }
   

    return render(request,'shop.html',context)




