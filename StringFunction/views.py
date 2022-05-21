from django.shortcuts import render

def index(request):
  if(request.method == 'POST'):
    return render(request, 'StringFunctionComplete.html')
  return render(request, 'StringFunction.html')