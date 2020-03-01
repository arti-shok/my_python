#https://drakonhub.com/ide/doc/arti-shok/2
import random
value = random.randint(1,4)
number = int(input('enter:\n'))
if number == value:
    print('u win')
elif number < value:
    print('conceived number is greater\ntry again')
else:
    print('conceived number is less\ntry again')
