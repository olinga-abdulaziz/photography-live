from django.shortcuts import render
from django.views import generic
from .models import Post,Category
from django.urls import reverse_lazy
from .forms import PostForm



class HomeView(generic.ListView):
    model=Post
    context_object_name='posts'
    template_name='core/home.html'

class AboutView(generic.TemplateView):
    template_name='core/about.html'


class ContactView(generic.TemplateView):
    template_name='core/contact.html'


class PotforlioView(generic.TemplateView):
    template_name='core/potforlio.html'


class AddpostView(generic.CreateView):
    template_name='core/addpost.html'
    form_class=PostForm
    model=Post
    success_url=reverse_lazy('home')


