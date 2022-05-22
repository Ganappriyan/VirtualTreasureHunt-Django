from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader

def index(request): # Render Page & Validation
  if(request.method == 'POST'):
    if(request.POST.get('done') == 'true'):
      return redirect('/3diff')
    key = request.POST.get('key')
    if(key in ('PASSWORD', 'password', 'WRONG', 'wrong', 'AGAIN', 'again')):
      return render(request, 'TryAgainComplete.html')
    return render(request, 'TryAgain.html', {'res':'TRY AGAIN', 'info':'YOUR PASSWORD IS WRONG'})
  return render(request, 'TryAgain.html')
