from django.shortcuts import render, redirect


def index(request):
    if(request.method == 'POST'):
        h1 = '' if (request.POST.get('q1') == 'o2') else 'Wrong Answer'
        h2 = '' if (sorted(request.POST.getlist('q2')) == [
            'o1', 'o2', 'o3', 'o4']) else 'Wrong Answer'
        h3 = '' if (request.POST.get('q3').lower()
                    == 'n') else 'Wrong Answer'
        
        if(h1 == h2 == h3 == ''):
            return redirect('/2.2tryb')
        return render(request, 'QnA2.html', {'h1': h1, 'h2': h2, 'h3': h3})

    return render(request, 'QnA2.html')
