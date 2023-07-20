questions = ['Should you subscribe', 'is coding cool', 'is 1+1=3', 'Is Luis cool']
answers = ['yes', 'yes', 'no','yes']


def quizGame():
  score = 0
  for i in range(len(questions)):
    print(questions[i])
    ans = input('Please answer \n')
    if ans == answers[i]:
      print ('Correct!!')
      score += 1
    else:
      print('Incorrect Fool')
      
  print(f'The final score is: {score}')
quizGame()
