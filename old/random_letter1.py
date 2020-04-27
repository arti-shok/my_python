list_of_words =  ['самовар', 'весна', 'лето']
from random import choice
word = choice(list_of_words)
letter = choice(word)
print(word.replace(letter,'?'))
enter_letter = input('enter letter: ')
if enter_letter == letter:
    print('u win!\nhidden word is', word)
else:
    print('try again')
