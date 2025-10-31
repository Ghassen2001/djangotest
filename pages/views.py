from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader

def homePageView(request):
    return HttpResponse("Welcome to the Home Page!")

def index(request):
    context = {"message": "Ahla bel GASTON"}
    template = loader.get_template("pages/index.html")
    return HttpResponse(template.render(context, request))


from .models import Book , Author

import requests
def listBooks(request):
    context ={"books": Book.objects.all()}
    return render(request,"pages/listBooks.html",context)

def show (request,book_id):
    context = {"book": get_object_or_404(Book, pk=book_id)}
    return render(request,"pages/show.html",context)

def add (request): 
    author=Author.objects.get(name="Victor Hugo")
    book=Book.objects.create(title="Dragon ball 3", quantity=12, author=author)
    return redirect("pages:listBooks")

def remove (request):
    book = Book.objects.filter(title__startswith="Dragon")
    book.delete()
    return redirect("pages/listBooks.html")

def edit (request):
    book = Book.objects.get(title ="Dragon ball 3")
    book.title="Dragon ball 6"
    book.save()
    return redirect("pages/listBooks.html")