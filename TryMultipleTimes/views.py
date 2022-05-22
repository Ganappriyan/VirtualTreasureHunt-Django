from django.shortcuts import redirect, render
from django.http import HttpResponse


def index(request): # Render Page & Validation
  if(request.method == 'POST'):
    done = request.POST.get('done')
    if(done=='true'):
      return redirect('/3diff') # TODO: Go to Next Page
    return render(request, 'TryMultipleTimesComplete.html')
  
  return render(request, 'TryMultipleTimes.html')
