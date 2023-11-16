from django.db.models import *
from .mixins import *
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User



class Contact(TimeStampMixin):
    firstname = CharField(max_length=200)
    lastname = CharField(max_length=200)
    number = CharField(max_length=200)
    email = CharField(max_length=200)
    message = TextField()
    
    def __str__(self) -> str:
        return self.firstname
    
    def get_absolute_url(self): 
        return reverse('index')
    


class Workers(Model):
    fullname = CharField(max_length=250)
    position = CharField(max_length=250)
    avatar = ImageField()
    
    def __str__(self):
        return self.fullname
    
class Reviews(Model):
    fullname = CharField(max_length=250)
    position = CharField(max_length=250)
    message = CharField(max_length=250)
    avatar = ImageField()
    def __str__(self):
        return self.fullname
   
class Blogs(Model):
    title = CharField(max_length=250)
    text = TextField()
    image = ImageField()
    created_at = DateTimeField(auto_now_add=True)
    author = ForeignKey( settings.AUTH_USER_MODEL,on_delete=CASCADE)
    def __str__(self):
        return self.title
    
class Category( Model):
    name = CharField(max_length=250)
    image = ImageField(null=True, blank=True)
    description = CharField(max_length=250)
class Brands( Model):
    name =  CharField(max_length=250)
    image =  ImageField(null=True, blank=True)
    description =  CharField(max_length=250)
class Products(Model):
    name =  CharField(max_length=250)
    description =  CharField(max_length=250)
    image =  ImageField()
    price =  FloatField()
    color =  CharField(max_length=250)
    weight =  FloatField()
    barcode =  CharField(max_length=250)
    categoryObject =  ForeignKey(Category, on_delete= CASCADE)
    brandObject =  ForeignKey(Brands, on_delete= CASCADE)
    created_at = DateTimeField(default=timezone.now,null=True)
    
    def discount(self):
        return self.price + self.price * 0.2
class ProductsRaitings(Model):
    productobject = ForeignKey(Products,on_delete=CASCADE)
    author = ForeignKey(settings.AUTH_USER_MODEL,on_delete=CASCADE)
    points = IntegerField()    
    
class ProductsImages( Model):
    productObject =  ForeignKey(Products, on_delete= CASCADE)
    image =  ImageField()

class ProductsLikes(Model):
    productobject = ForeignKey(Products,on_delete=CASCADE)
    author = ForeignKey(settings.AUTH_USER_MODEL,on_delete=CASCADE) 





class Tag(models.Model):
    name = models.CharField(max_length=255)

class Publicate(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    body = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)



class Subscription(models.Model):
    mail = models.TextField(max_length=255)
    


class Cart(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    productObject = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)