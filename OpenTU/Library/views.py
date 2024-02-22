from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Room, RoomTransaction, BookTransaction
from User.models import Student
from .forms import BookTransactionForm, RoomTransactionForm

TIME_SLOTS = {
    '0': '7:30 - 8:30',
    '1': '8:30 - 9:30',
    '2': '9:30 - 10:30',
    '3': '10:30 - 11:30',
    '4': '11.30 - 12:30',
    '5': '12:30 - 13:30',
    '6': '13:30 - 14:30',
    '7': '14:30 - 15:30',
    '8': '15:30 - 16:30',
    '9': '16:30 - 17:30',
    '10': '17:30 - 18:30',
    '11': '18:30 - 19:30',
    '12': '19:30 - 20:30',
    '13': '20:30 - 21:30',
    '14': '21:30 - 22:30',
    '15': '22:30 - 23:30',
}

@login_required
def library_request(request):
    context = {}

    books = Book.objects.all()
    for book in books:
        book.is_available = book.quantity - book.borrowers.count() > 0
    context['books'] = books

    rooms = Room.objects.all()
    for room in rooms:
        room.is_available = True
    context['rooms'] = rooms

    room_transaction = RoomTransaction.objects.filter(user=request.user)
    book_transaction = BookTransaction.objects.filter(user=request.user)
    history = []
    for each in room_transaction:
        history.append({
            'name': each.room.name, 
            'image': each.room.image, 
            'is_active': not each.is_close, 
            'create_date': each.create_date.strftime('%d %b %Y'),
            'info': f'Time : {TIME_SLOTS[each.timeslot]}'
            })
    for each in book_transaction:
        history.append({
            'name': each.book.name, 
            'image': each.book.image, 
            'is_active': not each.is_close, 
            'create_date': each.create_date.strftime('%d %b %Y'),
            'info': f'Addr : {each.address}'
            })
    context['history'] = history

    return render(request, 'Library/library.html', context)

@login_required
def borrow(request, id):

    if request.method == 'POST':
        form = BookTransactionForm(request.POST)
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
            'book': Book.objects.get(pk=id), 
            'form': BookTransactionForm()
        }
        return render(request, 'Library/borrow.html', context)

@login_required
def book_room(request, id):
    if request.method == 'POST':
        form = RoomTransactionForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            room = Room.objects.get(pk=id)
            form.room = room
            form.save()

            return redirect('/library')
    else:
        context = {
            'room': Room.objects.get(pk=id),
            'form': RoomTransactionForm()
        }
        return render(request, 'Library/room_booking.html', context)