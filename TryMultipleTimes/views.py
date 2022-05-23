from datetime import datetime
from django.shortcuts import redirect, render

from DB.models import Participants


def index(request): # Render Page & Validation
  if(request.method == 'POST'):
    done = request.POST.get('done')
    if(done=='true'):
      teamname = request.session['teamname']
      collegename = request.session['collegename']
      
      ctime = datetime.now().strftime("%H:%M:%S")
      
      data = Participants.objects.get(teamname=teamname)
      data.level2 = ctime
      data.save()
      
      return redirect('/3diff') # TODO: Go to Next Page
    return render(request, 'TryMultipleTimesComplete.html')
  
  return render(request, 'TryMultipleTimes.html')
