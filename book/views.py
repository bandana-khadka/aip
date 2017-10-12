from .models import Book
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import UserForm, BookForm
from django.contrib.auth import logout
from django.db.models import Q
from django.shortcuts import get_object_or_404


def index(request):

    all_books = Book.objects.all()

    query = request.GET.get("q")
    if query:
        all_books = all_books.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        ).distinct()

    if not request.user.is_authenticated():
        return render(request, 'book/home.html', {'all_books': all_books})
    else:
        return render(request, 'book/user/index.html', {'all_books': all_books})


def book_detail(request, book_id):

    book = get_object_or_404(Book, pk=book_id)

    if not request.user.is_authenticated():
        return render(request, 'book/details.html', {'book': book})
    else:
        return render(request, 'book/user/details.html', {'book': book})


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
            if user.is_active:
                login(request, user)
                all_books = Book.objects.all()
                return render(request, 'book/user/index.html', {'all_books': all_books})
            else:
                return render(request, 'book/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'book/login.html', {'error_message': 'Invalid login'})
    return render(request, 'book/login.html')


def register(request):

    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
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


def add_book(request):

    if not request.user.is_authenticated():
        return render(request, 'book/login.html')
    else:
        form = BookForm(request.POST or None)
        if form.is_valid():
            book = form.save(commit=False)
            book.name = form.cleaned_data['name']
            book.publication_address = form.cleaned_data['publication_address']
            book.edition = form.cleaned_data['edition']
            book.description = form.cleaned_data['description']
            book.publication_date = form.cleaned_data['publication_date']
            book.save()
            return render(request, 'book/user/details.html', {'book_description': book.description, 'book': book})
        context = {
            "form": form,
        }
        return render(request, 'book/user/new_book.html', context)


def edit_book(request, book_id):

    if not request.user.is_authenticated():
        return render(request, 'book/login.html')

    book = get_object_or_404(Book, pk=book_id)
    if(book):
        if(request.POST):
            book.name = request.POST['name']
            book.publication_address = request.POST['publication_address']
            book.edition = request.POST['edition']
            book.description = request.POST['description']
            book.publication_date = request.POST['publication_date']
            book.save()
            return render(request, 'book/user/details.html', {'book_description': book.description, 'book': book})
    else:
        return render(request, 'book/user/index.html', {'error_message': 'Invalid book!'})
    return render(request, 'book/user/edit_book.html', {'book': book})


def delete_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    books = Book.objects.all()
    return render(request, 'book/user/index.html', {'all_books': books})