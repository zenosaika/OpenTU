from django.forms import ModelForm
from .models import BookTransaction, RoomTransaction

class BookTransactionForm(ModelForm):
    class Meta:
        model = BookTransaction
        fields = ['duration', 'address']

class RoomTransactionForm(ModelForm):
    class Meta:
        model = RoomTransaction
        fields = ['timeslot']