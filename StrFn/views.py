from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request): # Render Page & Validation
  if(request.method == 'POST'):
    key = request.POST.get('key')
    print('\nKey: ', key)
    if(key == 'hello'):
      return render(request, 'index.html', {'res':'Well Done!!'}) # TODO: Go to Next Page
    return render(request, 'index.html', {'res':'Wrong Password'})
  
  return render(request, 'index.html')
