from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.models import User
import uuid
from .models import UserToken
from django.shortcuts import get_object_or_404


def request_reset_password(request):

    if request.method == "POST":
        email = request.POST['email']
        user = User.objects.get(email__iexact=email)
        if user is not None:
            if user.is_active:
                token = uuid.uuid4().hex
                user_token = UserToken()
                user_token.user = user
                user_token.token = token
                # user_token.save()
                # send_mail(
                #     'Reset your password',
                #     'Please go to the link http://127.0.0.1:8000/reset_password/' + user.id + '/' + token + ' to reset your password',
                #     'library@library.com',
                #     ['bandanarocks@gmail.com'],
                #
                return render(request, 'book/login.html', {'message': 'Please check your email. We have sent you a link to reset your password.'})
            else:
                return render(request, 'request_reset_password.html', {'error_message': 'No user found with the email address'})
        else:
            return render(request, 'request_reset_password.html', {'error_message': 'No user found with the email address'})

    return render(request, 'request_reset_password.html')


def reset_password(request):

    if request.method == "POST":

        user_id = request.POST['user_id']
        token = request.POST['token']
        password = request.POST['password']

        if(password != request.POST['confirm_password']):
            return render(request, 'reset_password.html',
                          {'error_message': 'Confirm your new password again. They do not match.',
                           'user_id': user_id,
                           'token': token
                           })
        user_token = get_object_or_404(UserToken, user_id=user_id, token=token)
        print(user_token)
        user_token.delete()
        user = get_object_or_404(User, pk=user_id)
        user.set_password(password)
        user.save()
        return render(request, 'book/login.html', {'message': 'Password changed successfully. Please login with you new Password'})

    else:
        return render(request, 'book/login.html', {'error_message': 'Something went wrong'})


def reset_password_form(request, user_id, token):

        user_id = request.GET['user_id']
        token = request.GET['token']
        return render(request, 'reset_password.html',
                      {'user_id': user_id,
                       'token': token
                       })

