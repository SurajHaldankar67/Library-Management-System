from .models import Book_Information
from django import forms

class Add_Book(forms.ModelForm):

    class Meta:
        model = Book_Information
        fields = "__all__"