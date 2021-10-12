from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post
from .forms import PostForm

# Create your views here.

# def home(request):
#   return render(request, 'home.html', {})

class HomePage(ListView):
  model= Post
  template_name= 'home.html'

class  BlogD(DetailView):
  model = Post
  template_name='p_detail.html'
