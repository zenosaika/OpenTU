from django.forms import ModelForm
from .models import Student

class StudentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['first_name'].initial = self.instance.first_name


    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone', 'image']