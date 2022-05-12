from django.shortcuts import render
from django.http import HttpResponse


count = 0

def index(request): # Render Page & Validation
  if(request.method == 'POST'):
    done = request.POST.get('done')
    if(done=='true'):
      return render(request, 'TryMultipleTimes.html') # TODO: Go to Next Page
    global count
    print('\nCount: ', count) # TODO: Remove tmp Line
    count+=1
    if(count > 10):
      return render(request, 'TryMultipleTimesComplete.html')
    if(count > 1):
      return render(request, 'TryMultipleTimes.html', {'res':'Wrong Password, TRY AGAIN!'})
  
  return render(request, 'TryMultipleTimes.html')
