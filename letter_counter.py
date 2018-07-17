"""This module consists of two functions that count letters in external file."""
import string
import timeit

def counter1(text):
    """This function counts letters from string text. Counter1 uses built-in count function."""
    count_dict = {}
    letters = list(string.ascii_letters)
    sum_of_letters = 0
    for i in letters:
        sum_of_letters = text.count(i, 0, -1)
        count_dict[i] = sum_of_letters
    return count_dict

def counter2(text):
    """This function counts letters from string text. Counter2 uses custom loop to count the characters in the text."""
    count_dict = {}
    for character in text:
        if character in string.ascii_letters:
            count_dict.setdefault(character,0)
            count_dict[character] = count_dict[character] + 1
    return count_dict


file = open('Pride&Prejudice.txt','r')
text = file.read()
counter1(text)
print("Counter1: ", timeit.timeit('counter1(text)', number = 10, globals=globals()))
counter2(text)
print("Counter2: ", timeit.timeit('counter2(text)', number = 10, globals=globals()))
