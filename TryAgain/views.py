from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

count=0
def index(request): # Render Page & Validation
  if(request.method == 'POST'):
    if(request.POST.get('done') == 'true'):
      print('Done: True')
      pass
    global count
    count += 1
    print('Count:',count)
    key = request.POST.get('key')
    print('\nKey: ', key) # TODO: Remove This Line
    if(key in ('PASSWORD', 'password', 'WRONG', 'wrong', 'AGAIN', 'again')):
      count = 0
      return render(request, 'TryAgainComplete.html')
    if(count>1):
      return render(request, 'TryAgain.html', {'res':'TRY AGAIN', 'info':'YOUR PASSWORD IS WRONG'})
  return render(request, 'TryAgain.html')
