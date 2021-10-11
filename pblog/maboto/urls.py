from  django.urls import path
from .views import HomePage,BlogD


urlpatterns = [
  # path('', views.home, name='home',),
  path('', HomePage.as_view(), name='home'),
  path('blog/<int:pk>', BlogD.as_view(), name='blog_detail' ),
]