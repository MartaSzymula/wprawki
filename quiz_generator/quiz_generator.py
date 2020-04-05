"""quiz_generator creates quizzes with questions ans answear in random order, each unique. Each quiz comes with answer key."""

import random
import re

source = 'C:/Python/ABSwP/Quiz_gen/capitals.txt'

base = {}

with open(source) as fh:
     base = dict(re.findall(r'\n?([^-]+)-\s+(.+)', fh.read())) #creates a dictionary with all capitals

#Generating 5 quizzes

for quizNum in range(5):
    quizFile = open('capitalsquiz%s.txt'%(quizNum+1), 'w')
    answerFile = open('answers%s.txt'%(quizNum+1), 'w')

    quizFile.write('Name:\n\nDate:\n\nCapitals Quiz\n\n\nChoose correct capital:\n\n')

    countries = list(base.keys())
    random.shuffle(countries)

    capitals = list(base.values())

    for i in countries:

        answers = {i: base[i]}
        answerFile.write(str(answers)+'\n') #writes the answer key to the file

        narrowCapitals = list(set(capitals) - {base[i]}) #random answer set without the correct answer
        ansSet = random.sample(narrowCapitals, k=3) + [base[i]] #chooses 3 random answers and adds the correct one

        random.shuffle(ansSet)
    
        finalSet = 'A. ' + ansSet[0] + ' B. ' + ansSet[1] + ' C. ' + ansSet[2] + ' D. ' + ansSet[3]

        quizFile.write(str(countries.index(i)+1) + '. ' + i + '\n' + finalSet + '\n\n')
