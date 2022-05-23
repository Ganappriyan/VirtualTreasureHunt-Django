from datetime import datetime
from django.shortcuts import redirect, render

from DB.models import Participants

def index(request):
    if(request.method == 'POST'):
        stime = datetime.now().strftime("%H:%M:%S")  # Gets Current Time
        request.session['stime'] = stime  # Stores Current time in Session

        teamname = request.POST.get('teamname')  # Gets Team Name from POST
        collegename = request.POST.get('collegename')
        request.session['teamname'] = teamname
        
        if(Participants.objects.filter(teamname=teamname).exists()):
            return render(request, 'home.html', {'cmd': 'Team Name Taken, Try Different Name'})
          
        data = Participants.objects.create(
            teamname=teamname, collegename=collegename, starttime1=stime)
        data.save()
        
        return redirect('/1.2qnac')
    return render(request, 'home.html')