from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def description(request):
    return render(request, 'generator/description.html')


def password(request):

    letters = string.ascii_letters.lower()

    if request.GET.get('length'):
        length = request.GET['length']
    else:
        length = 0

    if request.GET.get('uppercase'):
        letters += string.ascii_letters.upper()

    if request.GET.get('numbers'):
        letters += '1234567890'

    if request.GET.get('special'):
        letters += '!@#$%^&*()_+='

    the_password = ''.join(random.choice(letters) for i in range(int(length)))

    return render(request, 'generator/generatedPassword.html', {'password': the_password})

