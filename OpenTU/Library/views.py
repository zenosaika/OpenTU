from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from User.models import Student
from .forms import TransactionForm

def library_request(request):
    books = Book.objects.all()
    for book in books:
        book.is_available = book.quantity - book.borrowers.count() > 0
    context = {'books': books}
    return render(request, 'Library/library.html', context)

@login_required
def borrow(request, id):

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            book = Book.objects.get(pk=id)
            form.book = book
            form.save()

            # update Book
            student = Student.objects.get(user=request.user)
            book.borrowers.add(student)

            return redirect('/library')
    else:
        context = {
            'book_id': id, 
            'form': TransactionForm()
        }
        return render(request, 'Library/borrow.html', context)