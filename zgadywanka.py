import random
import math
minval=1
maxval=10
no=maxval-minval
chances=int(math.log(no,2))

secretnumber=random.randint(minval,maxval)

if chances<=4:
    odmiana='szanse.'
else:
    odmiana='szans.'
print('Zgadnij numer z przedziału od '+str(minval)+' do '+str(maxval)+'. Masz ' +str(chances)+' '+str(odmiana))

guesstaken=chances
while guesstaken>0:
    print('Podaj liczbę. Zostały ci '+str(guesstaken)+' szanse')
    guess=int(input())

    if guess<minval or guess>maxval:
        print('Liczba wykracza poza przedział!')
    elif guess<secretnumber:
        print('Liczba jest zbyt mała')
        guesstaken=guesstaken-1
    elif guess>secretnumber:
        print('Liczba jest zbyt duża')
        guesstaken=guesstaken-1
    else:
        break
if guess==secretnumber:
    print('Zgadłeś w '+str(guesstaken)+'. podejściu!')
else:
    print('Nie udało ci się! Numerem, o którym myślałem było '+str(secretnumber))
