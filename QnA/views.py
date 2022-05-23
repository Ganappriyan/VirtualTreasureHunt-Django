from datetime import datetime
from re import A
from django.shortcuts import redirect, render

from DB.models import Participants


def index(request):
    if(request.method == 'POST'):
        h1 = '' if (request.POST.get('q1') == 'o3') else 'Wrong Answer'
        h2 = '' if (sorted(request.POST.getlist('q2')) == [
                    'o1', 'o2', 'o3', 'o4']) else 'Wrong Answer'
        h3 = '' if (request.POST.get('q3').lower() in [
                    'prince', 'princes', 'princess']) else 'Wrong Answer'

        if(h1 == h2 == h3 == ''):
            teamname = request.session['teamname']

            ctime = datetime.now().strftime("%H:%M:%S")

            data = Participants.objects.get(teamname=teamname)
            data.level1 = ctime
            data.save()

            return redirect('/2.1try')
        return render(request, 'QnA.html', {'h1': h1, 'h2': h2, 'h3': h3})
    return render(request, 'QnA.html')
