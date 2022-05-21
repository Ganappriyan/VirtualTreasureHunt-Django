from random import choice
from django.shortcuts import render

def index(request):
  if(request.method == 'POST'):
    return render(request, 'CommentLineComplete.html')
  passwords = ['hi', 'hello', 'welcome', 'student', 'engineering']
  return render(request, 'CommentLine.html', {'pass':choice(passwords)})