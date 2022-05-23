import datetime
from django.shortcuts import redirect, render

from DB.models import Participants

def index(request): # Render Page & Validation
  if(request.method == 'POST'):
    if(request.POST.get('done') == 'true'):
      teamname = request.session['teamname']
      
      ctime = datetime.now().strftime("%H:%M:%S")
      
      data = Participants.objects.get(teamname=teamname)
      data.level2 = ctime
      data.save()
      
      return redirect('/3diff')
    key = request.POST.get('key')
    if(key in ('PASSWORD', 'password', 'WRONG', 'wrong', 'AGAIN', 'again')):
      return render(request, 'TryAgainComplete.html')
    return render(request, 'TryAgain.html', {'res':'TRY AGAIN', 'info':'YOUR PASSWORD IS WRONG'})
  return render(request, 'TryAgain.html')
