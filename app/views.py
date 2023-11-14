from django.shortcuts import *
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
    
    points = ProductsRaitings.objects.filter(productobject = row).count()
    likesCount = ProductsLikes.objects.filter(productobject = row).count()
    context = {
        'row':row,
        'images':images,
        'likesCount':likesCount,
        'points':points,
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

def pressLike(request,id):
    row = Products.objects.get(id = id)
    user = request.user
    isLiked =  ProductsLikes.objects.filter(productobject = row,author = user).exists()
  

    if not(request.user.is_authenticated):
        return  HttpResponseBadRequest("Пользователь не авторизован")
    if not(isLiked):
        return redirect('index')
  
   
    ProductsLikes.objects.create(productobject = row,author = user)
    return HttpResponse('успешно',status=200)

def setRating(request):

    # if not (request.method == 'POST'):
    #     return HttpResponseBadRequest('Такой страницы нет')
    
    if not(request.user.is_authenticated):
        return HttpResponseBadRequest('Пользователь не авторизован')
    
    user = request.user
    
    points = int(request.GET.get('points'))
    id = int(request.GET.get('id'))


    product = Products.objects.get(id=id)

    isLiked = ProductsRaitings.objects.filter(productobject = product, author = user).exists()
        
    if isLiked:
        row = ProductsRaitings.objects.get(productObject = product, author = user)
        row.points = points
        row.save()
        return HttpResponse("Оценка принята", status = 200)
    ProductsRaitings.objects.create(productobject = product, author = user, points=points)
    return HttpResponse("Оценка принята", status = 200)

def getRaiting(request,id):
    product = Products.objects.get(id = id)
    points = ProductsRaitings.objects.filter(productobject = product).aggregate(Avg('points'))['points__avg']
    
    return JsonResponse({'points':points})

    
  

def saveMail(request):
    points = request.POST.get('mail')
    Subscription.objects.create(mail = points)
    return redirect('index')


def myAccount(request):
    return render(request,'my-account.html')



def setCart(request):
        
    if not(request.user.is_authenticated):
        return HttpResponseBadRequest('Пользователь не авторизован')
    return render(request,'cart.html')


def cart(request):
        
    if not(request.user.is_authenticated):
        return HttpResponseBadRequest('Пользователь не авторизован')
    
    user = request.user
    rows = Cart.objects.filter(author = user)
    totalPrice = 0
    for i in rows:
        totalPrice =+ i.quantity

    context = {
        'rows':rows,
        'totalPrice':totalPrice,
    }
    return render(request,'cart.html',context)


















