import math

def task1(text="Count stuff in this random sentence."):
    """Function task1 counts vowels, consonants and words occurence in a given text."""

    print(text)
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    consonants = list('bcdfghjklmnpqrstvwxyz')
    sum_of_vowels = 0
    sum_of_consonants = 0
    for i in vowels:
        print(str(i) + ': ' + str(text.count(i, 0, -1)))
        sum_of_vowels = sum_of_vowels + text.count(i, 0, -1)
    print('Sum of vowels:' + str(sum_of_vowels))
    for a in consonants:
        sum_of_consonants = sum_of_consonants + text.count(a, 0, -1)
    print('Sum of consonants:' + str(sum_of_consonants))
    print('Number of words: ' + str(len(text.split(' '))))

def task2(minval=1,maxval=100):
    """Function task2 prints to the console all even numbers from a griven range"""
    even_numbers = []
    for i in range(1, 100):
        if i%2 == 0:
            even_numbers.append(i)
    print(even_numbers)

def task3(maxval=100):
    """Function taks3 prints to the console prime numbers from a given range"""
    prime = []
    num_table = list(range(0, maxval+1))
    for i in range(2, int(math.sqrt(maxval))):
        if num_table[i] != 0:
            for j in range (i**2, maxval+1, i):
                num_table[j] = 0
    for i in num_table:
        if i != 0 and i > 1:
            prime.append(i)
    print(prime)

def task4(text='long text to revert'):
    """Function task4 reverts given text"""
    to_revert = list(text)
    print(text)
    reverted = []
    for i in range(len(to_revert), 0, -1):
        reverted.append(to_revert[i-1])
    print(''.join(reverted))

def task5(a=4, b=1, c=7):
    """Function task5 derives roots from a quadratic equation"""
    x1 = 0
    x2 = 0
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b - math.sqrt(delta))/2*a
        x2 = (-b + math.sqrt(delta))/2*a
        print('Roots are:')
        print(x1, x2)
    if delta is 0:
        x1 = -b/2*a
        print(x1)
    if delta < 0:
        square_delta = 1j*math.sqrt(4*a*c - b**2)
        new_delta = -delta
        imaginary = math.sqrt(new_delta)/2*a
        x1 = -b - imaginary*1j
        x2 = -b + imaginary*1j
        print(x1, x2)

def task6(a=[1,2,12,4], b=[2,4,2,9]):
    """Function task6 counts dot (scalar) product of tw vectors"""
    product = 0
    if len(a) == len(b):
        for i in range(0, len(a)):
            component = a[i] * b[i]
            product = product + component
        print(product)
    else:
        print('Multipication impossible')

# def task7()

if __name__ == '__main__':
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
