from random import choice
from django.http import response
from django.shortcuts import redirect, render

def index(request):
  if('pass' in request.COOKIES):
    print("Cookies: ", request.COOKIES['pass'])  #TODO: Remove
  
  if(request.method == 'POST'):
    print("Pass: ", request.POST.get('password')) # TODO: Remove
    password = request.POST.get('password')
    if(password == request.COOKIES['pass']):
      return render(request, 'TryDifferentViewComplete.html')
    return render(request, 'TryDifferentView.html', {'pass': password, 'cmd': 'Wrong Password'})
  
  password = choice(['free fire', 'don don don', 'shawarma', 'addict', 'pubg'])
  print('New Password: ', password) # TODO: Remove
  response = render(request, 'TryDifferentView.html', {'pass': password})
  response.set_cookie(key='pass', value=password)
  return response