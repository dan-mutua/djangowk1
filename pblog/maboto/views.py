from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.

# def home(request):
#   return render(request, 'home.html', {})

class HomePage(ListView):
  model= Post
  template_name= 'home.html'

class  BlogD(DetailView):
  model = Post
  template_name='p_detail.html'


class UpdateViewB(UpdateView):
  model = Post
  template_name= 'update.html'
  fields = ('title', 'author','body')

class DeleteViewB(DeleteView):
  model = Post
  template_name= 'delete.html'
  success_url= reverse_lazy('home')