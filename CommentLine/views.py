from random import choice
from django.shortcuts import redirect, render

def index(request):
  if(request.method == 'POST'):
    return redirect('/5')
  passwords = ['hi', 'hello', 'welcome', 'student', 'engineering']
  return render(request, 'CommentLine.html', {'pass':choice(passwords)})