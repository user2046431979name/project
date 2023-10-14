from django.db.models import *
from .mixins import *
from django.utils import timezone
from django.urls import reverse






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