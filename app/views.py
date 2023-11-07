from django.shortcuts import render
from .models import *
from django.views.generic import ListView,DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.core.paginator import Paginator

from django.contrib.auth import get_user_model
from django.contrib.auth import login,logout

from django.http import *
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
    products = Products.objects.all()
    brands = Brands.objects.all()
    begin_price = 0
    end_price = 10231120
    if request.GET.get('begin_price'):
        begin_price = request.GET.get('begin_price')
        
    if request.GET.get('end_price'):
        end_price = request.GET.get('end_price')
      

    

    page = 1
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
       

    if request.GET.get('page'):
        page = int(request.GET.get('page'))
    
    products = Products.objects.all().filter(name__contains = search,price__range = (begin_price,end_price))

    paginator = Paginator(products,2)
    next_page = page + 1 if (page) < len(paginator.page_range) else 1
    previos_page = page - 1 if (page - 1) != 0 else page
    
    
    context = {
        'result_count':f'Showing {15} of {len(products)} results',
        'categories':Category.objects.all(),
        'products':paginator.page(page),
        'page':paginator.page_range,
        'nextP':next_page,
        'previosP':previos_page,
        'brands':brands
        
    }
   

    return render(request,'shop.html',context)

def like(request,id):
 
  

    if not(request.user.is_authenticated):
        return  HttpResponseBadRequest("Пользователь не авторизован")
    
    row = Products.objects.get(id = id)
    user = request.user
    isLiked = ProductsLikes.objects.filter(productobject = row,author = user).exists()
    if not(isLiked):
        return HttpResponseBadRequest('уже нажимали')
    ProductsLikes.objects.create(productobject = row,author = user)
    return HttpResponse('успешно',status=200)

def setRaiting(request):
    if not(request.method == 'POST'):
        return HttpResponseBadRequest('такой страницы нет')


    if not(request.user.is_authenticated):
        return HttpResponseBadRequest('пользователь не авторизован')
    

    user = request.user
    points = int(request.POST.get('points')) 
    id = int(request.POST.get('id'))
    row = Products.objects.get(id = id)
    isRaiting = ProductsRaitings.objects.filter(productobject = row,author = user).exists()
    if not(isRaiting):
        return HttpResponseBadRequest('уже нажимали')
    ProductsRaitings.objects.create(productobject = row,author = user,points=points)
    return HttpResponse('успешно',status=200)




def login_view(request):
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return login_view(request)







