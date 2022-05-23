from datetime import datetime
from django.shortcuts import render
from random import choice

from DB.models import Finalers


def index(request):
    if(request.method == 'POST'):
        teamname = request.session['teamname']
      
        ctime = datetime.now().strftime("%H:%M:%S")
      
        data = Finalers.objects.get(teamname=teamname)
        stime = data.starttime2
      
        diff = datetime.strptime(ctime, "%H:%M:%S") - \
                datetime.strptime(stime, "%H:%M:%S")
      
        data.level5 = ctime
        data.totaltime2 = diff
        data.save()
        
        return render(request, 'StringFunctionComplete.html')
    passwords = ['narocoo@@ggo', 'ldie@fldgor@lako', 'peuiv@gerevr@vene', 'atperep@eeslt@ea', 'annmro@iami@']
    return render(request, 'StringFunction.html', {'password': choice(passwords)})
