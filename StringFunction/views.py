from django.shortcuts import render
from random import choice


def index(request):
    if(request.method == 'POST'):
        return render(request, 'StringFunctionComplete.html')
    passwords = ['narocoo@@ggo', 'ldie@fldgor@lako', 'peuiv@gerevr@vene', 'atperep@eeslt@ea', 'annmro@iami@']
    return render(request, 'StringFunction.html', {'pass': choice(passwords)})
