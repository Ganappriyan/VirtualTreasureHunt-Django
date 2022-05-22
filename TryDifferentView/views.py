from random import choice
from django.shortcuts import redirect, render

def index(request):
  password = 'valimai'
  if(request.method == 'POST'):
    if(request.POST.get('password') == password):
      return render(request, 'TryDifferentViewComplete.html')
    return render(request, 'TryDifferentView.html', {'pass': password, 'cmd': 'Wrong Password'})
  return render(request, 'TryDifferentView.html', {'pass': password})