from django.shortcuts import render
from .models import *
from django.views.generic import ListView,DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView



class index(ListView):
    template_name = 'index.html'




class contact(CreateView):
    model = Contact
    template_name = 'contact.html'
    fields = ['firstname', 'lastname', 'number','email','message']


