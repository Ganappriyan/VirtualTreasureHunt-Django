from datetime import datetime
from random import choice
from django.shortcuts import render

from DB.models import Participants

def index(request):
  if('pass' in request.COOKIES):
    print("Cookies: ", request.COOKIES['pass'])  #TODO: Remove
  
  if(request.method == 'POST'):
    password = request.POST.get('password')
    
    if(password == request.COOKIES['pass']):
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
    
    return render(request, 'TryDifferentView.html', {'pass': password, 'cmd': 'Wrong Password'})
  
  password = choice(['free fire', 'don don don', 'shawarma', 'addict', 'pubg'])
  response = render(request, 'TryDifferentView.html', {'pass': password})
  response.set_cookie(key='pass', value=password)
  return response