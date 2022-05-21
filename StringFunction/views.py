from django.shortcuts import render
from random import choice


def index(request):
    if(request.method == 'POST'):
        return render(request, 'StringFunctionComplete.html')
    passwords = ['go go corona', 'hello', 'welcome', 'student', 'narocoo@@ggo']
    return render(request, 'StringFunction.html', {'pass': choice(passwords)})
