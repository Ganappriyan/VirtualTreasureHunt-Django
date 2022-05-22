from django.shortcuts import redirect, render
from django.http import HttpResponse


count = 0

def index(request): # Render Page & Validation
  if(request.method == 'POST'):
    done = request.POST.get('done')
    if(done=='true'):
      return redirect('/3diff') # TODO: Go to Next Page
    global count
    count+=1
    if(count > 8):
      return render(request, 'TryMultipleTimesComplete.html')
    if(count > 1):
      return render(request, 'TryMultipleTimes.html', {'res':'Wrong Password, TRY AGAIN!'})
  
  return render(request, 'TryMultipleTimes.html')
