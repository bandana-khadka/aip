from .models import Book
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import UserForm, BookForm
from django.contrib.auth import logout
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer

# Function to check whether the username exists
def username_exists(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
# if the username alreadu exists it pops messgae saying username already exists
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists. Please enter a new username.'

    return JsonResponse(data)

# Function to check the email address of the user 
def email_exists(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': User.objects.filter(email__iexact=email).exists()
    }
# pops message saying email address already registered if email account exists
    if data['is_taken']:
        data['error_message'] = 'This email address is already registered. Please enter a new email address.'

    return JsonResponse(data)

# Goes to the homepage and retreive all the books in the library
def index(request):

    all_books = Book.objects.all()

    query = request.GET.get("q")
    if query:
        all_books = all_books.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(author__icontains=query)
        ).distinct()

    if not request.user.is_authenticated():
        return render(request, 'book/home.html', {'all_books': all_books})
    else:
        return render(request, 'book/user/index.html', {'all_books': all_books})

# Retreive required book information 
def book_detail(request, book_id):

    book = get_object_or_404(Book, pk=book_id)

    if not request.user.is_authenticated():
        return render(request, 'book/details.html', {'book': book})
    else:
        return render(request, 'book/user/details.html', {'book': book})

# user logged out back to login page
def logout_user(request):

    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'book/login.html', context)


def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            
            # Function to check whether user is active or not
            # If user acive 
            if user.is_active:
                login(request, user)
                all_books = Book.objects.all()
                return render(request, 'book/user/index.html', {'all_books': all_books})
            
            # If user not active
            else:
                return render(request, 'book/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'book/login.html', {'error_message': 'Invalid login'})
    return render(request, 'book/login.html')

# Function to register new user using User name and password
def register(request):

    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        
# Function to authenticate registering username and password
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                books = Book.objects.all()
                return render(request, 'book/user/index.html', {'books': books})
    context = {
        "form": form,
    }
    return render(request, 'book/register.html', context)

# Function to add books to the library
def add_book(request):

    if not request.user.is_authenticated():
        return render(request, 'book/login.html')
    else:
        form = BookForm(request.POST or None)
        if form.is_valid():
            book = form.save(commit=False)
            
            # Function to add new book details like name 
            book.name = form.cleaned_data['name']
            
            # Function to add book's publication address
            book.publication_address = form.cleaned_data['publication_address']
            
            # Function to add book edition
            book.edition = form.cleaned_data['edition']
            
            # Function to add book description
            book.description = form.cleaned_data['description']
            
            # Function to add book publication date
            book.publication_date = form.cleaned_data['publication_date']
            
            
            # Function to add book Author details
            book.author = form.cleaned_data['author']
            
            # Function to save new book details creation
            book.save()
            return render(request, 'book/user/details.html', {'book_description': book.description, 'book': book})
        context = {
            "form": form,
        }
        return render(request, 'book/user/new_book.html', context)

# Function to edit book information
def edit_book(request, book_id):

    if not request.user.is_authenticated():
        return render(request, 'book/login.html')

    book = get_object_or_404(Book, pk=book_id)
    if(book):
        if(request.POST):
            # edit book name 
            book.name = request.POST['name']
            
            # edit publication address
            book.publication_address = request.POST['publication_address']
            
            # edit book edition
            book.edition = request.POST['edition']
            
            # edit book description
            book.description = request.POST['description']
            
            # edit publication date
            book.publication_date = request.POST['publication_date']
            
            # edit author details 
            book.author = request.POST['author']
            
            # post save after editing book informations
            book.save()
            return render(request, 'book/user/details.html', {'book_description': book.description, 'book': book})
    else:
        return render(request, 'book/user/index.html', {'error_message': 'Invalid book!'})
    return render(request, 'book/user/edit_book.html', {'book': book})

# Function to delete book information
def delete_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    books = Book.objects.all()
    return render(request, 'book/user/index.html', {'all_books': books})

# Function to list all books using rest API
class BookList(APIView):

    def get(self, request):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)

    def post(self, request):
        # To test rest API function
        if(request.POST['auth_key'] == 'ABCD!@#$'):
            all_books = Book.objects.all()
            serializer = BookSerializer(all_books, many=True)
            return Response(serializer.data)
        else:
            return Response('Error')
