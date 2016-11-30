import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New \
   Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West \
   Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
    #create the quiz and answer key files.
    quizFile = open('quiz'+str(quizNum+1)+'.txt','w')
    keyFile = open('key'+str(quizNum+1)+'.txt', 'w')
    #write out the header for the quiz.
    quizFile.write('This is quiz ' + str(quizNum+1) + '\n\n')
    #shuffle the order of the states.
    capkeys=list(capitals.keys())
    random.shuffle(capkeys)
    #write questions
    for questionNumber in range(50):
        quizFile.write(str(questionNumber+1) + '. What is the capital of ' + capkeys[questionNumber] + '?\n')
        wrongAnswers=list(capitals.values())
        correctAnswer = capitals[capkeys[questionNumber]]
        random.shuffle(wrongAnswers)
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers=random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        for option in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[option], answerOptions[option]))
        keyFile.write(str(questionNumber + 1) + '. %s\n' % ('ABCD'[answerOptions.index(correctAnswer)]))
        quizFile.write('\n')
        quizFile.close
        keyFile.close

  
       