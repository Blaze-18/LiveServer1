from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('meow',views.meow,name='meow')
]