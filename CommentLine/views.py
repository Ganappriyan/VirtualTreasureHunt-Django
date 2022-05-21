from random import choice
from django.shortcuts import redirect, render

def index(request):
  if(request.method == 'POST'):
    return redirect('/f2strfn')
  passwords = ['hi', 'hello', 'welcome', 'student', 'engineering']
  return render(request, 'CommentLine.html', {'pass':choice(passwords)})