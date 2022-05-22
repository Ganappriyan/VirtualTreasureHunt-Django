from django.shortcuts import redirect, render


def index(request):
    if(request.method == 'POST'):
        h1 = '' if (request.POST.get('q1') == 'o3') else 'Wrong Answer'
        h2 = '' if (sorted(request.POST.getlist('q2')) == [
            'o1', 'o2', 'o3', 'o4']) else 'Wrong Answer'
        h3 = '' if (request.POST.get('q3').lower()
                    in ['princes', 'princess']) else 'Wrong Answer'
        if(h1 == h2 == h3 == ''):
            return redirect('/2.1try')
        return render(request, 'QnA.html', {'h1': h1, 'h2': h2, 'h3': h3})

    return render(request, 'QnA.html')
