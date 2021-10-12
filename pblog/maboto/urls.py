from  django.urls import path
from .views import HomePage,BlogD,UpdateViewB


urlpatterns = [
  # path('', views.home, name='home',),
  path('', HomePage.as_view(), name='home'),
  path('blog/<int:pk>', BlogD.as_view(), name='blog_detail' ),
  path('article/edit/<int:pk>', UpdateViewB.as_view(), name="updateb"),
]