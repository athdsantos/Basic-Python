import random, time
numberTyped = int(input('Type a number between 0 and 5: '))
print('Thinking...')
time.sleep(2)
numberRandom = random.randint(0, 5)
if numberTyped == numberRandom:
    print('Congrats bro, you are right, the number typed {}, is equal like mine, {}.'.format(numberTyped, numberRandom))
else:
    print('Ohhh no, you are wrong, the number typed {}, is not equal like mine, {}.'.format(numberTyped, numberRandom))
