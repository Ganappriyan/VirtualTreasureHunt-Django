from django.shortcuts import redirect, render

def index(request):
  if(request.method == 'POST'):
    return redirect('/1.1qna')
  return render(request, 'home.html')