from DB.models import Participants
from datetime import datetime
from django.shortcuts import redirect, render

from DB.models import Finalers


def index(request):
    if(request.method == 'POST'):
        stime = datetime.now().strftime("%H:%M:%S")  # Gets Current Time
        request.session['stime'] = stime  # Stores Current time in Session

        teamname = request.POST.get('teamname')  # Gets Team Name from POST
        collegename = request.POST.get('collegename')
        phoneno = request.POST.get('phoneno')
        request.session['teamname'] = teamname

        if(Finalers.objects.filter(teamname=teamname).exists()):
            return render(request, 'home.html', {'cmd': 'Team Name Taken, Try Different Name'})

        data = Finalers.objects.create(
            teamname=teamname, collegename=collegename, starttime2=stime, phoneno=phoneno)
        data.save()

        return redirect('/f1insp')
    return render(request, 'home.html')
