from random import choice
from django.shortcuts import redirect, render
password = choice(['kgf', 'valimai', 'beast'])

def index(request):
  global password
  if(request.method == 'POST'):
    if(request.POST.get('password') == password):
      return redirect('/f1insp')
    return render(request, 'TryDifferentView.html', {'pass': password, 'cmd': 'Wrong Password'})
  
  return render(request, 'TryDifferentView.html', {'pass': password})