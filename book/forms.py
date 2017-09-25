from django.contrib.auth.models import User
from django import forms
from .models import Book, Author
from django.views.generic.edit import UpdateView

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['name', 'publication_address', 'edition', 'description', 'publication_date']

class BookUpdateForm(UpdateView):

    class Meta:
        model = Book
        fields = ['name', 'publication_address', 'edition', 'description', 'publication_date']