from django.shortcuts import render
from .models import Book

def library_request(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'Library/library.html', context)