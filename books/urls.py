from django.urls import path
from books.views import bookshome , aboutfun ,contactusfun

urlpatterns = [
    path('home', bookshome, name="home"),
    path('about', aboutfun , name="about"),
    path('contact', contactusfun , name="contact"),

    
]