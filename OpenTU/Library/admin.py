from django.contrib import admin
from .models import Book, BookTransaction, Room, RoomTransaction

admin.site.register(Book)
admin.site.register(BookTransaction)
admin.site.register(Room)
admin.site.register(RoomTransaction)