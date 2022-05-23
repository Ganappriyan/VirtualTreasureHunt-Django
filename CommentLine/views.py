from datetime import datetime
from random import choice
from django.shortcuts import redirect, render

from DB.models import Finalers

def index(request):
  if(request.method == 'POST'):
    teamname = request.session['teamname']
    
    ctime = datetime.now().strftime("%H:%M:%S")
    
    data = Finalers.objects.get(teamname=teamname)
    data.level4 = ctime
    data.save()
    
    return redirect('/f2strfn')
  passwords = ['hakuna matata', 'virtual treasure hunt', 'stop wait go', 'i am waiting', 'believer']
  return render(request, 'CommentLine.html', {'pass':choice(passwords)})