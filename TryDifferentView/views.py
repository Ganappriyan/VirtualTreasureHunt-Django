from datetime import datetime
from random import choice
from django.shortcuts import render

from DB.models import Participants

def index(request):
  if(request.method == 'POST'):
    typedPassword = request.POST.get('password')
    actualPassword = request.session['actualPassword']
    
    if(typedPassword == actualPassword):
      teamname = request.session['teamname']
      
      ctime = datetime.now().strftime("%H:%M:%S")
      
      data = Participants.objects.get(teamname=teamname)
      stime = data.starttime1
      
      diff = datetime.strptime(ctime, "%H:%M:%S") - \
                datetime.strptime(stime, "%H:%M:%S")
      
      data.level3 = ctime
      data.totaltime1 = diff
      data.save()
      
      return render(request, 'TryDifferentViewComplete.html')
    
    return render(request, 'TryDifferentView.html', {'pass': actualPassword, 'cmd': 'Wrong Password'})
  
  actualPassword = choice(['free fire', 'don don don', 'shawarma', 'addict', 'pubg'])
  request.session['actualPassword'] = actualPassword
  return render(request, 'TryDifferentView.html', {'pass': actualPassword})
