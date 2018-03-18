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
    """Function task6 counts dot (scalar) product of two vectors"""
    product = 0
    if len(a) == len(b):
        for i in range(0, len(a)):
            component = a[i] * b[i]
            product = product + component
        print(product)
    else:
        print('Multipication impossible')

def task7(n=8):
    """task7 generates a dictionary of n pairs which are (i, i*i)
    and prints it"""
    dictionary=dict()
    for i in range (1, n+1):
        dictionary[i] = i*i
    print(dictionary)

def task8(to_replace='two 755 ff'):
    """Function task8 converts numbers in variable to their text
    equivalents. If there is already such text equivalent, Function
    leaves it there."""
    numbers = {
    '0' : "zero",
    '1' : "one",
    '2' : "two",
    '3' : "three",
    '4' : "four",
    '5' : "five",
    '6' : "six",
    '7' : "seven",
    '8' : "eight",
    '9' : "nine"
    }

    len_to_replace = str(to_replace)
    text = ''
    list_elements = len_to_replace.split()

    for n in range (0, len(list_elements)):
        if list_elements[n] in numbers.values():
            text = text + ' ' + str(list_elements[n])

        else:
            for i in range (0, len(list_elements[n])):
                if list_elements[n][i] in numbers:
                    text = text + ' ' + str(numbers[list_elements[n][i]])

    text = text.strip()
    print(text)
    return text

def task9(x1=[3.5, 4.5], x2=None):
    """Function task9 counts the average of two numbers & standard
    deviation .

    Parameters
    ----------
    x1 : list or float, default [3.5, 4.5]
        If x1 is a list, then x2 is omitted.
    x2 : float or None, default None

    Returns
    -------
    float
        Returned object is average of given parameters.
    """
    num_list = []
    if type(x1) is list:
        num_list = x1
    else:
        num_list = [x1, x2]
    list_sum = 0
    for i in range(0, len(num_list)):
        num_float = float(num_list[i])
        list_sum = list_sum + num_float
    average = list_sum / len(num_list)
    print("Average = " + str(average))

    deviations = 0
    for n in range(0, len(num_list)):
        deviations = deviations + (num_list[n]-average)**2
    st_deviation = math.sqrt(deviations/(len(num_list)-1))
    print("Standard deviation = " + str(st_deviation))
    return average

if __name__ == '__main__':
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    # task7()
    task8()
    # task9()
