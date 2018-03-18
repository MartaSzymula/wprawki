import string
import timeit
def counter1(text):
    # """ """
    count1 = {}
    letters = list(string.ascii_letters)
    sum_of_letters = 0
    for i in letters:
        sum_of_letters = text.count(i, 0, -1)
        count1[i] = sum_of_letters
    # print(count1)

    # print('\n')

def counter2(text):
    count2 = {}
    for character in text:
        if character in string.ascii_letters:
            count2.setdefault(character,0)
            count2[character] = count2[character] + 1
    # print(count2)

file = open('Pride&Prejudice.txt','r')
text = file.read()
counter1(text)
print("Counter1: ", timeit.timeit('counter1(text)', number = 1000, globals=globals()))
counter2(text)
print("Counter2: ", timeit.timeit('counter2(text)', number = 1000, globals=globals()))
