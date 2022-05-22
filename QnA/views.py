from django.shortcuts import render

def index(request):
  ques = [['The average of 20 numbers is zero. Of them, at the most, how many may be greater than zero?',
               'Engineering is a,',
               'What is Full Form of "GOOGLE"?'],
               ['Spot the odd one out - FIRST, SECOND, THIRD, FORTH, FIFTH, SIXTH, SEVENTH, EIGHTH',
                '',
                '']]
  c = 0
  return render('QnA.html', {'q1': ques[c][0], 'q2': ques[c][1], 'q3': ques[c][2]})
