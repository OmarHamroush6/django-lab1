from django.shortcuts import render
from django.http import HttpResponse , JsonResponse

# Create your views here.
def bookshome(request):
    booksinfo = [
		{"id":1, "name":"book1", "description":"book1_description"},
		{"id":2, "name":"book2", "description":"book2_description"},
		{"id":3, "name":"book3", "description":"book3_description"}
    ]
    return render(request,"books/bookshome.html",context={"booksinfo" : booksinfo})

def aboutfun(request):
    return render(request,"books/about.html")

def contactusfun(request):
    return render(request,"books/contactus.html")
