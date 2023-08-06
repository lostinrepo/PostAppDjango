from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Person,Post
from django.urls import reverse_lazy

class HomePage(ListView):
    model = Post 
    template_name = "home.html"

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"

class CreatePost(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title","author","body"]

class UpdatePost(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title","author","body"]

class DeletePost(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")

class AboutPage(TemplateView):
    template_name = "about.html"

# Create your views here.
