#from django.shortcuts import render
from .models import Book
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import logout

# Create your views here.
from django.http import HttpResponse


def index(request):

    all_books = Book.objects.all()
    html = ''
    for book in all_books:
        url = '/book/' + str(book.id) + '/'
        html += '<a href="' + url + '">' + book.name + '</a><br>'

    # return HttpResponse("Hello, world. You're at the books index.")
    return HttpResponse(html)

def detail(request, book_id):
    return HttpResponse("<h2>Details for Book ID: " + str(book_id) + "</h2>")

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
                return render(request, 'book/index.html', {'all_books': all_books})
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
                books = Book.objects.filter(user=request.user)
                return render(request, 'book/index.html', {'books': books})
    context = {
        "form": form,
    }
    return render(request, 'book/register.html', context)