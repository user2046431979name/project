from django.db.models import *
from .mixins import *
from django.utils import timezone
from django.urls import reverse
from django.conf import settings





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

