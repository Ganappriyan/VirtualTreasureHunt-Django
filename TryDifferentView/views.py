from random import choice
from django.shortcuts import redirect, render
password = choice(['kgf', 'valimai', 'beast'])

def index(request):
  global password
  if(request.method == 'POST'):
    if(request.POST.get('password') == password):
      return render(request, 'TryDifferentViewComplete.html')
    password = choice(['kgf', 'valimai', 'beast'])
    return render(request, 'TryDifferentView.html', {'pass': password, 'cmd': 'Wrong Password'})
  password = choice(['kgf', 'valimai', 'beast'])
  return render(request, 'TryDifferentView.html', {'pass': password})