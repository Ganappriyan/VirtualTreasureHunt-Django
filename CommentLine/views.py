from random import choice
from django.shortcuts import redirect, render

def index(request):
  if(request.method == 'POST'):
    return redirect('/f2strfn')
  passwords = ['hakuna matata', 'virtual treasure hunt', 'stop wait go', 'i am waiting', 'believer']
  return render(request, 'CommentLine.html', {'pass':choice(passwords)})