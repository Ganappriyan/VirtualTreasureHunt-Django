from datetime import datetime
from django.shortcuts import redirect, render

from DB.models import Participants


def index(request):
    if(request.method == 'POST'):
        stime = datetime.now().strftime("%H:%M:%S")  # Gets Current Time
        request.session['stime'] = stime  # Stores Current time in Session
        print('STime: ', stime)  # TODO Remove

        teamname = request.POST.get('teamname')  # Gets Team Name from POST
        collegename = request.POST.get('collegename')
        
        if(Participants.objects.filter(teamname=teamname).exists()):
            return render(request, 'home.html', {'cmd': 'Team Name Taken, Try Different Name'})
          
        data = Participants.objects.create(
            teamname=teamname, collegename=collegename, starttime=stime)
        data.save()
        
        request.session['teamname'] = teamname
        request.session['collegename'] = collegename
        
        return redirect('/1.1qna')
    return render(request, 'home.html')
